#lang racket

;; Advent of Code Day 5
(require htdp-trace)
(define raw (file->list "d05input.txt"))

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



(define points (convert raw))


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


;; produces the points horizpair overlaps
;; Pair -> (listof Coord)
(define (x-gen horizpair)
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


;; produces the points vertpair overlaps
(define (y-gen vertpair)
  (local
    [(define y1 (second vertpair))
     (define y2 (fourth vertpair))
     (define x (first vertpair))
     
     (define n (+ (abs (- y2 y1)) 1))

     (define (list-points lower n)
       (cond
         [(= n 0)
          empty]
         [else
          (cons (list x lower)
                (list-points (add1 lower) (sub1 n)))]))]

    (cond
      [(< y1 y2)
       (list-points y1 n)]
      [else
       (list-points y2 n)])))

;; adds coord to dict, updates otherwise
(define (dict-add coord dict)
  (cond
    [(empty? dict)
     (list (list (first coord)
                 (second coord)
                 1))]
    [(coord=? coord (first dict))
     (cons (list (first coord)
                 (second coord)
                 (add1 (third (first dict))))
           (rest dict))]
    [else
     (cons (first dict)
           (dict-add coord (rest dict)))]))

;; true if same coord, false otherwise
(define (coord=? one two)
  (and (= (first one) (first two))
       (= (second one) (second two))))

;; adds lst of elements to dict
(define (dict-lst lst dict)
  (cond
    [(empty? lst)
     dict]
    [else
     (dict-lst (rest lst) (dict-add (first lst) dict))]))


(define (fast-add lst dict)
  (cond
    [(empty? lst)
     dict]
    [else
     (fast-add (rest lst) (cons (first lst) dict))]))

;; returns dict of all overlapped points
(define (x-lines lines dict)
  (cond
    [(empty? lines)
     dict]
    [else
     (x-lines (rest lines) (fast-add (x-gen (first lines)) dict))]))

(define x (x-lines horiz-lines empty))

(define (y-lines lines dict)
  (cond
    [(empty? lines)
     dict]
    [else
     (y-lines (rest lines) (fast-add (y-gen (first lines)) dict))]))

(define y (y-lines vert-lines x))

;; produces how many elements in dict are duplicated
(define (dedup dict checked appeared)
  (cond
    [(empty? dict)
     (set-count checked)]
    [(set-member? checked (first dict))
     (dedup (rest dict)
            checked
            appeared)]
    [(set-member? appeared (first dict))
     (dedup (rest dict)
            (set-add checked (first dict))
            appeared)]
    [else
     (dedup (rest dict)
            checked
            (set-add appeared (first dict)))]))


;; Answer: 6283
(define p1ans (dedup y (set) (set)))



;; Part 2:

(define diag-lines (filter (lambda (x)
                             (and (not (horiz-line? x))
                                  (not (vert-line? x))))
                           points))


;; produces the points pair overlaps
(define (diag-gen pair)
  (local
    [(define x1 (first pair))

     (define y1 (second pair))

     (define x2 (third pair))

     (define y2 (fourth pair))

     (define n (+ (abs (- y2 y1)) 1))

     (define m (/ (- y2 y1) (- x2 x1)))

     (define (list-points x y n)
       (cond
         [(= n 0)
          empty]
         [else
          (cons (list x y)
                (list-points (add1 x) (add1 y) (sub1 n)))]))

     (define (neg-lp x y n)
       (cond
         [(= n 0)
          empty]
         [else
          (cons (list x y)
                (neg-lp (add1 x) (sub1 y) (sub1 n)))]))]

    (cond
      [(> m 0) ; positive slope
       (cond
         [(< x1 x2)
          (list-points x1 y1 n)]
         [else
          (list-points x2 y2 n)])]
      [else
       (cond
         [(< x1 x2)
          (neg-lp x1 y1 n)]
         [else
          (neg-lp x2 y2 n)])])))


;; adds all diag overlaps
(define (diags lines dict)
  (cond
    [(empty? lines)
     dict]
    [else
     (diags (rest lines) (fast-add (diag-gen (first lines)) dict))]))

(define all (diags diag-lines y))


;; Answer: 18864
(define p2ans (dedup all (set) (set)))