;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-lambda-reader.ss" "lang")((modname d9) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor mixed-fraction #f #t none #f () #t)))
;; Advent of Code Day 9

(require "d9input.rkt")

(define (convert lst)
  (cond
    [(empty? lst)
     empty]
    [else
     (cons (lon (string->list (fix-num (first lst))))
           (convert (rest lst)))]))

;; leading zeroes
(define (fix-num num)
  (cond
    [(< num (expt 10 99))
     (string-append "0" (number->string num))]
    [else
     (number->string num)]))

;; convert list of chars to ints
(define (lon loc)
  (cond
    [(empty? loc)
     empty]
    [else
     (cons (- (char->integer (first loc)) 48)
           (lon (rest loc)))]))


(define heightmap (convert input))


;; gets risk levels of two processing above and below rows
;;   (one and three respectively), in lockstep
;;   only gets risk levels of inner points
(define (risk one two three)
  (risk/acc (rest one)
            (rest two)
            (rest three)
            (first two)))


(define (risk/acc one two three comp)
  (cond
    [(empty? (rest one))
     0]
    [else
     (local
       [(define test (first two))]
       (cond
         [(and (< test (first one))
               (< test (first three))
               (< test (second two))
               (< test comp))
          (+ (add1 test) (risk/acc (rest one)
                                   (rest two)
                                   (rest three)
                                   test))]
         [else
          (risk/acc (rest one)
                    (rest two)
                    (rest three)
                    test)]))]))

;; get risk levels of all inner points in height
(define (risk-inners heights)
  (cond
    [(empty? (rest (rest heights)))
     0]
    [else
     (+ (risk (first heights)
              (second heights)
              (third heights))
        (risk-inners (rest heights)))]))


;; edge cases of horiz
(define (risk-edge one two)
  (risk-edge/acc (rest one) (rest two) (first one)))


(define (risk-edge/acc one two comp)
  (cond
    [(empty? (rest one))
     0]
    [else
     (local [(define test (first one))]
       (cond
         [(and (< test (first two))
               (< test (second one))
               (< test comp))
          (+ (add1 test)
             (risk-edge/acc (rest one)
                            (rest two)
                            test))]
         [else
          (risk-edge/acc (rest one)
                         (rest two)
                         test)]))]))


;; get the last two elements of lst
(define (last-two lst)
  (cond
    [(empty? (rest (rest lst)))
     lst]
    [else
     (last-two (rest lst))]))


(define bottom-two (last-two heightmap))

(define bottom-risk (risk-edge (second bottom-two) (first bottom-two)))

(define top-risk (risk-edge (first heightmap) (second heightmap)))

(define total-inner (+ top-risk (risk-inners heightmap) bottom-risk))


;; get risk of edge
(define (left-edge one two three)
  (local [(define test (first two))]
    (cond
      [(and (< test (first one)) ; up
            (< test (second two)) ; right
            (< test (first three))) ; down
       (add1 test)]
      [else
       0])))


;; one two three are 2-element lists of the last 2 elements
(define (right-edge one two three)
  (local [(define test (second two))]
    (cond
      [(and (< test (second one))
            (< test (first two))
            (< test (second three)))
       (add1 test)]
      [else
       0])))


;; get risk levels of all on left edge except corners
(define (risk-lefts heights)
  (cond
    [(empty? (rest (rest heights)))
     0]
    [else
     (+ (left-edge (first heights)
                   (second heights)
                   (third heights))
        (risk-lefts (rest heights)))]))


;; get risk levels of all on right edge except corners
(define (risk-rights heights)
  (cond
    [(empty? (rest (rest heights)))
     0]
    [else
     (+ (right-edge (last-two (first heights))
                    (last-two (second heights))
                    (last-two (third heights)))
        (risk-rights (rest heights)))]))


(define all-less-corners (+ total-inner
                            (risk-lefts heightmap)
                            (risk-rights heightmap)))

;; Answer (verify corners manually, none are low points)
(check-expect all-less-corners 530)