open System
open System.IO

type Direction =
    | Up of int
    | Down of int
    | Forward of int

let instantiate<'t> (name: string) parameters: 't =
    let lower = name.ToLower() in
    Reflection.FSharpType.GetUnionCases typeof<'t>
    |> Seq.find (fun x -> x.Name.ToLower() = lower)
    |> (fun ucase -> Reflection.FSharpValue.MakeUnion (ucase, parameters))
    :?> 't

let parse () : seq<Direction> =
    File.ReadAllLines "../input/day2.txt"
    |> Seq.map (fun a -> a.Split())
    |> Seq.map (fun a -> (a.[0], a.[1]))
    |> Seq.map (fun (a, b) -> (instantiate<Direction> a) [|int b|])

let data = parse()

let day1 (data: Direction seq) =
    let map (x, y) dir =
        match dir with
            | Up i      -> (x, y - i)
            | Down i    -> (x, y + i)
            | Forward i -> (x + i, y)
    
    let x, y = Seq.fold map (0, 0) data
    
    x * y
    
let day2 (data: Direction seq) =
    let map (x, y, aim) dir =
        match dir with
            | Up i      -> (x, y, aim - i)
            | Down i    -> (x, y, aim + i)
            | Forward i -> (x + i, y + aim * i, aim)
            
    let x, y, aim = Seq.fold map (0, 0, 0) data
    
    x * y
    
    
data |> day1 |> printfn "Day 1: %d" 
data |> day2 |> printfn "Day 2: %d" 
