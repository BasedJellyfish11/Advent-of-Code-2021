open System.IO

let parse () =
    File.ReadAllLines "../../input/day1.txt"
    |> Seq.map (fun x -> x.Trim())
    |> Seq.map int
    
let day1 (inp: seq<int>) : int =
    inp
    |> Seq.pairwise
    |> Seq.filter (fun (x, y) -> y > x)
    |> Seq.length
    
let day2 (inp: seq<int>) : int =
    inp
    |> Seq.windowed 3
    |> Seq.map Seq.sum
    |> Seq.pairwise
    |> Seq.filter (fun (x, y) -> y > x)
    |> Seq.length
    
let inp = parse()

inp |> day1 |> printfn "Day1: %d"
inp |> day2 |> printfn "Day2: %d"