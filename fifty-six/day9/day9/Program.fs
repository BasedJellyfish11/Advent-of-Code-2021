
open System
open System.Collections
open System.IO

let parse () =
    let lines = File.ReadAllLines "../input/day9.txt"
    
    lines
        |> Seq.map (fun x -> x.Trim())
        |> Seq.map (Seq.map int)
        |> Seq.map (Seq.map (fun a -> a - int('0')))
        |> Seq.toArray
        |> array2D
        
        
let getOpt x y (arr2D: int[,]) =
    if 0 <= x && x < arr2D.GetLength(0) && 0 <= y && y < arr2D.GetLength(1) then
        Some(arr2D.[x, y])
    else
        None
        
let lows nums =
    nums
    |> Array2D.mapi (fun x y e ->
        let low =
            seq { (-1, 0); (1, 0); (0, -1); (0, 1) }
            |> Seq.where (fun (a, b) -> (a, b) <> (0, 0))
            |> Seq.map (fun (a, b) -> getOpt (x + a) (y + b) nums)
            |> Seq.filter Option.isSome
            |> Seq.map Option.get
            |> Seq.forall (fun a -> e < a)
            
        if low then Some(x, y) else None
    )
    |> Seq.cast<(int * int) option>
    |> Seq.filter Option.isSome
    |> Seq.map Option.get
    
let p1 nums =
    lows nums
        |> Seq.map (fun (a, b) -> nums.[a, b] + 1)
        |> Seq.sum
        
let p2 nums =
    let low_points = lows nums
    
    let rec floodfill (x, y) collector start =
        match getOpt x y nums with
            | Some(e) when e >= start && e <> 9 && not <| Set.contains (x, y) collector ->
                let collector = Set.add (x, y) collector
                
                seq { (-1, 0); (1, 0); (0, -1); (0, 1) }
                    |> Seq.filter (fun (a, b) -> (a, b) <> (0, 0))
                    |> Seq.fold (fun acc (a, b) -> Set.union acc <| floodfill (x + a, y + b) acc start) collector
                    
            | _ -> Set.empty
    
    low_points
        |> Seq.map (fun (a, b) -> floodfill (a, b) Set.empty nums[a, b])
        |> Seq.map Set.count
        |> Seq.sortDescending
        |> Seq.take 3
        |> Seq.fold (fun acc e -> acc * e) 1
    
    
let nums = parse()
p1 nums |> printfn "Part1 : %d"
p2 nums |> printfn "Part2 : %A"