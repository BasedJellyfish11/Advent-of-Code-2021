;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-lambda-reader.ss" "lang")((modname d5) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor mixed-fraction #f #t none #f () #t)))
;; Advent of Code Day 5

(require "d5input.rkt")

;; Part 1

;; A Coord is a (list Nat Nat)

;; A Pair is a (list Nat Nat Nat Nat)
;;   representing two coordinates x1, y1, and x2, y2

;; produces a list from the first 4 elements of lst
;; (listof Nat) -> Pair
(define (first-pair lst)
  (cond
    [(empty? lst)
     empty]
    [else
     (local
       [(define (keep lst n)
          (cond
            [(= n 0)
             empty]
            [else
             (cons (first lst)
                   (keep (rest lst) (sub1 n)))]))]

       (keep lst 4))]))


;; produces a list from everything but the first 4 elements of lst
;; (listof Nat) -> (listof Nat)
(define (rest-pairs lst)
  (foldr (lambda (x rror)
           (rest rror))
         lst (build-list 4 +)))


;; convert the input to a list of pairs of each coordinate pair
;; (listof Nat) -> (listof Pair)
(define (convert lst)
  (cond
    [(empty? lst)
     empty]
    [else
     (cons (first-pair lst)
           (convert (rest-pairs lst)))]))



(define points (convert input))


;; produces true if pair is a horiz line and false otherwise
(define (horiz-line? pair)
  (= (second pair)
     (fourth pair))) ; y1 = y2


;; produces true if pair is a vert line and false otherwise
(define (vert-line? pair)
  (= (first pair)
     (third pair))) ; x1 = x2



(define horiz-lines (filter (lambda (x)
                              (horiz-line? x))
                            points))



(define vert-lines (filter (lambda (x)
                              (vert-line? x))
                            points))



;; produces all pairs of elements with one_i, two
(define (cross one two)
   (foldr (lambda (x rror) ; x from one
            (append (foldr (lambda (y rror2) ; y from two
                             (cons (list x y)
                                   rror2))
                           empty two)
                    rror))
          empty one))

;; all possible points in a 1000x1000 grid from (0,0) to (1000,1000)
(define coords (cross (build-list 1000 +) (build-list 1000 +)))



;; produces the points horizpair overlaps
;; Pair -> (listof Coord)
(define (overlaps horizpair)
  (local
    [(define x1 (first horizpair))
     (define x2 (third horizpair))
     (define y (second horizpair))

     (define n (+ (abs (- x2 x1)) 1))

     (define (list-points lower n)
       (cond
         [(= n 0)
          empty]
         [else
          (cons (list lower y)
                (list-points (add1 lower) (sub1 n)))]))]
    (cond
      [(< x1 x2)
       (list-points x1 n)]
      [else
       (list-points x2 n)])))



