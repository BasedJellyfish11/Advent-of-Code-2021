;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-lambda-reader.ss" "lang")((modname d14input) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor mixed-fraction #f #t none #f () #t)))
(require "provide.rkt")
(provide polymer)
(provide rules)
(provide expoly)
(provide ex-rules)

(define polymer (string->list "KFVHFSSVNCSNHCPCNPVO"))

(define rawrules '(KS -> O
SP -> V
OH -> F
VC -> P
BO -> S
CV -> H
FO -> N
KV -> V
OV -> B
NB -> K
FS -> F
KB -> N
HK -> C
VP -> B
SV -> S
FP -> P
BS -> B
BP -> K
OS -> K
PB -> C
HB -> H
VN -> S
FB -> C
OC -> N
OO -> F
PC -> O
FK -> K
OP -> V
BH -> C
NP -> C
KF -> H
SK -> F
HN -> O
CB -> O
SN -> N
VF -> S
KC -> H
HF -> V
NC -> P
BN -> F
KO -> C
PS -> B
HO -> S
CH -> O
KP -> K
VK -> V
BB -> V
BF -> P
CS -> K
CN -> H
PK -> C
SH -> O
BC -> H
FN -> N
BK -> N
PN -> B
PO -> O
SC -> S
NO -> S
KN -> O
VB -> C
SF -> H
FH -> C
FF -> B
VO -> S
PH -> F
CK -> B
FC -> P
VV -> F
VH -> O
OF -> O
HP -> K
CO -> V
VS -> V
SB -> F
SS -> K
CF -> O
OK -> V
ON -> B
NS -> H
SO -> B
NV -> V
NH -> B
NN -> K
KH -> H
FV -> B
KK -> N
OB -> F
NK -> F
CC -> S
PP -> B
PF -> H
HC -> P
PV -> F
BV -> N
NF -> N
HV -> S
HH -> C
HS -> O
CP -> O))


(define (firstrule raw)
  (local
    [(define (keep-n lst n)
       (cond
         [(= n 0)
          empty]
         [else
          (cons (first lst)
                (keep-n (rest lst) (sub1 n)))]))]

    (keep-n raw 3)))


(define (restrules raw)
  (foldr (lambda (x rror)
           (rest rror))
         raw (build-list 3 +)))


(define (convert raw)
  (cond
    [(empty? raw)
     empty]
    [else
     (cons (firstrule raw)
           (convert (restrules raw)))]))


(define rules (convert rawrules))

(define expoly (string->list "NNCB"))

(define exrules '(CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C))

(define ex-rules (convert exrules))