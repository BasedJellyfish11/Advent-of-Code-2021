;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-lambda-reader.ss" "lang")((modname d7) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor mixed-fraction #f #t none #f () #t)))
;; Advent of Code Day 6

(require "d7input.rkt")

(define (median lst)
  (local
    [(define slst (quicksort lst >))
     (define n (length lst))

    (define (halfway n lst)
      (cond
        [(<= n 0)
         (first lst)]
        [else
         (halfway (- n 2) (rest lst))]))]

  (halfway n slst)))
    
(define (energy lst move)
  (map (lambda (x)
         (abs (- x move)))
       lst))

(define (totenergy lst)
  (foldr (lambda (x rror)
           (+ x rror))
         0 lst))

;; Answer
(check-expect (totenergy (energy input (median input))) 337833)


(define (mean lst acc len)
    (cond
      [(empty? lst)
       (/ acc len)]
      [else
       (mean (rest lst) (+ acc (first lst)) (add1 len))]))


(define goal (floor (mean input 0 0)))

(define (bigenergy pos end)
  (local
    [(define n (abs (- pos end)))]

    (/ (* n (add1 n)) 2)))


(define energylst (map (lambda (x)
                         (bigenergy x goal))
                       input))

(define totenergy2 (foldr (lambda (x rror)
                           (+ x rror))
                         0 energylst))

;; Answer
(check-expect totenergy2 96678050)
