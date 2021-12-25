#lang racket

;; Advent of Code Day 16

(define raw-input
  (string->list (symbol->string (first (file->list "d16input.txt")))))

;; Char -> (listof Nat)
(define (hex-to-bin char)
  (cond
    [(char=? char #\0)
     (list 0 0 0 0)]
    [(char=? char #\1)
     (list 0 0 0 1)]
    [(char=? char #\2)
     (list 0 0 1 0)]
    [(char=? char #\3)
     (list 0 0 1 1)]
    [(char=? char #\4)
     (list 0 1 0 0)]
    [(char=? char #\5)
     (list 0 1 0 1)]
    [(char=? char #\6)
     (list 0 1 1 0)]
    [(char=? char #\7)
     (list 0 1 1 1)]
    [(char=? char #\8)
     (list 1 0 0 0)]
    [(char=? char #\9)
     (list 1 0 0 1)]
    [(char=? char #\A)
     (list 1 0 1 0)]
    [(char=? char #\B)
     (list 1 0 1 1)]
    [(char=? char #\C)
     (list 1 1 0 0)]
    [(char=? char #\D)
     (list 1 1 0 1)]
    [(char=? char #\E)
     (list 1 1 1 0)]
    [(char=? char #\F)
     (list 1 1 1 1)]))

;; takes list of char (hex) and produces list of nat (bin)
(define (convert raw)
  (cond
    [(empty? raw)
     empty]
    [else
     (append (hex-to-bin (first raw))
             (convert (rest raw)))]))

;; real input
(define input (convert raw-input))


;; Some general purpose functions

;; keeps the first n elements of lst
(define (keep n lst)
  (cond
    [(= n 0)
     empty]
    [else
     (cons (first lst)
           (keep (sub1 n) (rest lst)))]))

;; removes the first n elements of lst
(define (remove n lst)
  (foldr (lambda (x rror)
           (rest rror))
         lst (build-list n +)))

;; returns decimal rep of list of bin numbers
(define (bin-to-dec lst)
  (local
    [(define len (length lst))]

    (foldl (lambda (x y rror)
             (+ (* x y) rror))
           0
           (reverse lst)
           (build-list len (lambda (z)
                             (expt 2 z))))))


;; Part 1:

;; produces the version number of packet
(define (ver-num packet)
  (bin-to-dec (keep 3 packet)))

;; produces the type id of packet
(define (typeid packet)
  (bin-to-dec (keep 3 (remove 3 packet))))


;; produces true if a literal value and false otherwise
(define (litval? packet)
  (= 4 (typeid packet)))


;; returns true if length id is 0, false otherwise
(define (len0id? packet)
  (= 0 (seventh packet)))


;; given a litval's groups of 5, parses it until it ends
(define (parse-litval packet)
  (cond
    [(= 0 (first packet))
     (keep 5 packet)]
    [else
     (append (keep 5 packet)
             (parse-litval (remove 5 packet)))]))


;; returns true if packet is not a litval and has len 0 id
(define (len-giver? packet)
  (and (not (litval? packet))
       (len0id? packet)))


;; returns true if packet is not a litval and has len 1 id
(define (num-giver? packet)
  (and (not (litval? packet))
       (not (len0id? packet))))


;; returns true if lst is all 0
(define (all-zero? lst)
  (foldr (lambda (x rror)
           (and x rror))
         true
         (map (lambda (y)
                (= 0 y)) lst)))


;; returns a list of all packets in input
(define (packet-structure input)
  (cond
    [(or (empty? input)
         (all-zero? input))
     empty]
    [(litval? input)
     (local
       [(define val (append (keep 6 input)
                            (parse-litval (remove 6 input))))
        (define val-len (length val))]

       (cons val (packet-structure (remove val-len input))))]
    [(len-giver? input)
     (cons (keep 22 input)
           (packet-structure (remove 22 input)))]
    [(num-giver? input)
     (cons (keep 18 input)
           (packet-structure (remove 18 input)))]))


;; sums all version numbers of the packets in packets
(define (sum-versions packets)
  (cond
    [(empty? packets)
     0]
    [else
     (+ (ver-num (first packets))
        (sum-versions (rest packets)))]))

(define packets (packet-structure input))

;; 951
(define answer (sum-versions packets))


;; Part 2:
;; returns the operation of packet
(define (functype packet)
  (local
    [(define type (typeid packet))]

    (cond
      [(= type 0)
       +]
      [(= type 1)
       *]
      [(= type 2)
       min]
      [(= type 3)
       max]
      [(= type 5)
       >]
      [(= type 6)
       <]
      [(= type 7)
       =])))


;; returns the value of a litval
(define (get-val litval)
  (local
    [(define groups (remove 6 litval))

     (define (remove-5n lst)
       (cond
         [(empty? lst)
          empty]
         [(= 0 (remainder (length lst) 5))
          (remove-5n (rest lst))]
         [else
          (cons (first lst)
                (remove-5n (rest lst)))]))]

    (bin-to-dec (remove-5n groups))))


;; returns the 15-bit field of a length 0 id
(define (15-field packet)
  (keep 15 (remove 7 packet)))


;; returns the 11-bit field of a length 1 id
(define (11-field packet)
  (keep 11 (remove 7 packet)))


;; returns information about a packet
(define (process packet)
  (cond
    [(litval? packet)
     (list (length packet) 'val
           (get-val packet))]
    [(len-giver? packet)
     (list (length packet) 'len
           (functype packet)
           (bin-to-dec (15-field packet)))]
    [else
     (list (length packet) 'num
           (functype packet)
           (bin-to-dec (11-field packet)))]))


;; a human parseable form
(define pack-list (map (lambda (x) (process x)) packets))


;; me when i evaluate everything manually
(define p2answer
  (+ 0 19891 1980 46326753392 0 0 0 0 14 16512012 1940294
     11 102 4 0 1246 0 6142500 154 1 0 243 5802101 0 10866823
     12238353 0 246 42862 33309 9499716882 0 0 969238 24800
     39967 97236731 2677 0 3 166 3266498235 5 841484756498
     1469052151 3360 56493 2 3276 10 2737 0 111))