;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-lambda-reader.ss" "lang")((modname d14) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor mixed-fraction #f #t none #f () #t)))
;; Advent of Code Day 14

(require "d14input.rkt")

;; Part 1
;; gets the middle insertion char from two outer chars
(define (input one two rules)
  (local
    [(define str (list->string (list one two)))

     (define sym (string->symbol str))

     (define (lookup sym rules)
       (cond
         [(symbol=? sym (in (first rules)))
          (out (first rules))] ; symbol
         [else
          (lookup sym (rest rules))]))

     (define output (lookup sym rules))

     (define to-str (symbol->string output))]

    (first (string->list to-str))))


;; input pair to a rule
(define (in rule)
  (first rule))


;; output char of a rule
(define (out rule)
  (third rule))


;; applies the rules once
(define (iteration polymer rules)
  (cond
    [(empty? (rest (rest polymer)))
     (list (first polymer)
           (input (first polymer) (second polymer) rules)
           (second polymer))]
    [else
     (cons (first polymer)
           (cons (input (first polymer) (second polymer) rules)
                 (iteration (rest polymer) rules)))]))


;; applies the rules n times
(define (iterate n polymer rules)
  (cond
    [(= n 0)
     polymer]
    [else
     (iterate (sub1 n) (iteration polymer rules) rules)]))


;; adds char to dict, increments val if already in dict
(define (add-dict char dict)
  (cond
    [(empty? dict)
     (list (list char 1))]
    [(char=? char (first (first dict)))
     (cons (list char (add1 (second (first dict))))
           (rest dict))]
    [else
     (cons (first dict)
           (add-dict char (rest dict)))]))


;; returns dict of each char count
(define (counts polymer dict)
  (cond
    [(empty? polymer)
     dict]
    [else
     (counts (rest polymer) (add-dict (first polymer) dict))]))


;; sorts dict by decreasing occurrence count
(define (occurrence-sort letters)
  (quicksort letters (lambda (x y)
                       (> (second x)
                          (second y)))))


;; sorted occurrences of polymer 10th iteration dict
(define sorted-counts
  (occurrence-sort (counts (iterate 10 polymer rules) empty)))


;; returns max minus min element of dict
(define (max-min sorted)
  (local
    [(define (last lst)
       (cond
         [(empty? (rest lst))
          (first lst)]
         [else
          (last (rest lst))]))

     (define max (second (first sorted)))

     (define min (second (last sorted)))]

    (- max min)))

;; Answer
(check-expect (max-min sorted-counts) 2509)



;; Part 2
;; adds a pair to dict
;; Char Char Dict -> Dict
(define (pair-add one two dict)
  (local
    [(define pair (list->string (list one two)))]

    (add pair 1 dict)))


;; adds pair to dict
(define (add pair count dict)
  (cond
    [(empty? dict)
     (list (list pair count))]
    [(string=? pair (first (first dict)))
     (cons (list pair (+ count (second (first dict))))
           (rest dict))]
    [else
     (cons (first dict)
           (add pair count (rest dict)))]))


;; setup input
(define (pair-count polymer dict)
  (cond
    [(empty? (rest polymer))
     dict]
    [else
     (pair-count (rest polymer)
                 (pair-add (first polymer) (second polymer) dict))]))


;; produces the two new pairs from pair and the inserted char
(define (make-pairs pair rules)
  (local
    [(define (middle rules)
       (cond
         [(symbol=? (string->symbol pair) (in (first rules)))
          (out (first rules))]
         [else
          (middle (rest rules))]))

     (define one (substring pair 0 1))

     (define two (substring pair 1 2))

     (define insert (symbol->string (middle rules)))]

    (list (string-append one insert)
          (string-append insert two))))
  

;; updates dict for each string in dict by count
(define (update lst count dict)
  (cond
    [(empty? lst)
     dict]
    [else
     (update (rest lst) count (add (first lst) count dict))]))


;; Dict -> Dict
(define (step polymer rules)
  (foldr (lambda (x rror)
           (update (make-pairs (first x) rules)
                   (second x)
                   rror))
         empty polymer))


;; performs n steps
;; Nat Dict Rules -> Dict
(define (step-until n polymer rules)
  (cond
    [(= n 0)
     polymer]
    [else
     (step-until (sub1 n) (step polymer rules) rules)]))


(define (char-count char n dict)
  (cond
    [(empty? dict)
     (list (list char n))]
    [(char=? char (first (first dict)))
     (cons (list char (+ n (second (first dict))))
           (rest dict))]
    [else
     (cons (first dict)
           (char-count char n (rest dict)))]))


(define (all-pairs lst dict)
  (cond
    [(empty? lst)
     dict]
    [else
     (all-pairs (rest lst)
                (char-count (first (string->list (first (first lst))))
                            (second (first lst))
                            dict))]))

;; initial input
(define init-pairs (pair-count polymer empty))

(define init-ex (pair-count expoly empty))

(define final-pair-counts (step-until 40 init-pairs rules))

(define sorted-char-counts
  (occurrence-sort (all-pairs final-pair-counts empty)))

;; Answer
(check-expect (add1 (max-min sorted-char-counts)) 2827627697643)
