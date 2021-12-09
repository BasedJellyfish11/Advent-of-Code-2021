open System
open System.IO

type Board = { board: int []; marked: bool [] }

let wins (board: bool []) =
    let rows = seq { for i in 0 .. 4 -> seq { for j in 0 .. 4 -> board.[5 * i + j] } }
    let cols = seq { for i in 0 .. 4 -> seq { for j in 0 .. 4 -> board.[5 * j + i] } }

    let any_all s = s |> Seq.map (Seq.forall id) |> Seq.exists id

    any_all rows || any_all cols


let parse () =
    let lines = File.ReadAllLines("../input/day4.txt")

    let nums =
        lines
        |> Seq.head
        |> (fun x -> x.Split ",")
        |> Seq.map int
        |> Seq.toList

    let boards =
        lines
        // Skip initial numbers
        |> Seq.skip 1
        // Remove empty lines between boards
        |> Seq.filter (String.IsNullOrWhiteSpace >> not)
        |> Seq.chunkBySize 5
        // Join lines for a board
        |> Seq.map (fun x -> String.Join(" ", x))
        // Split into ints
        |> Seq.map (fun x -> x.Split([| ' ' |], StringSplitOptions.RemoveEmptyEntries))
        |> Seq.map (Seq.map int)
        |> Seq.map
            (fun x ->
                { board = Seq.toArray x
                  marked = Array.zeroCreate 25 })

    nums, boards

let winner boards =
    boards |> Seq.filter (fun b -> wins b.marked)

let apply_n n boards =
    boards
    |> Seq.map (fun b -> (b, Seq.tryFindIndex ((=) n) <| b.board))
    |> Seq.map
        (fun (board: Board, num_opt) ->
            match num_opt with
            | Some num -> Array.set board.marked num true
            | None -> ()

            board)

let score board num =
    let sum =
        Seq.zip board.board board.marked
        |> Seq.filter (fun (_, marked) -> not marked)
        |> Seq.map fst
        |> Seq.sum

    sum * num

let split l =
    match l with
    | h :: t -> h, t
    | _ -> failwith "empty list!"


let part1 (nums: int list) init_boards =
    let rec run nums boards : (int * Board) option =
        let head, tail = split nums
        let boards = apply_n head boards

        Seq.tryHead <| winner boards
        |> Option.map (fun win -> head, win)
        |> Option.orElseWith (fun () -> run tail boards)

    let num, board = Option.get (run nums init_boards)
    score board num

let part2 nums init_boards =
    let rec run nums boards winning =
        match nums with
        | [] -> winning
        | head :: tail ->
            let boards = apply_n head boards |> Set
            
            let winners = winner boards |> Set
            
            let boards, winning =
                match Seq.tryLast <| winners with
                | Some win -> Set.difference boards winners, Some(win, head)
                | None -> (boards, winning)

            run tail boards winning

    let board, num = Option.get <| run nums (Set <| init_boards) None
    
    score board num

let nums, boards = parse ()
part1 nums boards |> printfn "Part1: %d"
part2 nums boards |> printfn "Part2: %d"
