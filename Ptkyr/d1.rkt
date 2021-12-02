;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-lambda-reader.ss" "lang")((modname d1) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor mixed-fraction #f #t none #f () #t)))
(require "d1input.rkt")

(define comp (append (rest input) (list 0))) ; lmao

;; (count-ups one two) produces how many elements of one are
;;   greater than the corresponding element of two
;; count-ups: (listof Num) (listof Num) -> Nat
(define (count-ups one two)
  (foldr (lambda (x y rror) 
           (cond
             [(> x y)
              (+ 1 rror)]
             [else
              rror]))
         0 two one))

;; Answer
(check-expect (count-ups input comp) 1482)


;; ******
;; Part 2
;; ******

(define comp2 (append (rest comp) (list 0)))

;; (moving-average one two three) sums the elements in one two and three
;; moving-average: (listof Num) (listof Num) (listof Num) -> (listof Num) 
(define (moving-average one two three)
  (foldr (lambda (x y z rror)
           (cons (+ x y z)
                 rror))
         empty one two three))

(define comp3 (moving-average input comp comp2))
(define comp4 (append (rest comp3) (list 0))) ; lmfao

;; Answer
(check-expect (count-ups comp3 comp4) 1518)