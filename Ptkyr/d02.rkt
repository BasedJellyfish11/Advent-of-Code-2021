;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-lambda-reader.ss" "lang")((modname d2) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor mixed-fraction #f #t none #f () #t)))
;; Advent of Code Day 2

(require "d2input.rkt")

;; ******
;; Part 1
;; ******

(define (func lst pos depth)
  (cond
    [(empty? lst)
     (* pos depth)]
    [(symbol=? 'up (first lst))
     (func (rest (rest lst))
            pos
            (- depth (second lst)))]
    [(symbol=? 'down (first lst))
     (func (rest (rest lst))
            pos
            (+ depth (second lst)))]
    [else
     (func (rest (rest lst))
            (+ pos (second lst))
            depth)]))

;; Answer
(check-expect (func input 0 0) 2019945)



;; ******
;; Part 2
;; ******

(define (thing lst pos depth aim)
  (cond
    [(empty? lst)
     (* pos depth)]
    [(symbol=? 'up (first lst))
     (thing (rest (rest lst))
            pos
            depth
            (- aim (second lst)))]
    [(symbol=? 'down (first lst))
     (thing (rest (rest lst))
            pos
            depth
            (+ aim (second lst)))]
    [else
     (thing (rest (rest lst))
            (+ pos (second lst))
            (+ depth (* aim (second lst)))
            aim)]))

;; Answer
(check-expect (thing input 0 0 0) 1599311480)