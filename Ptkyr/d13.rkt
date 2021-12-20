;; Advent of Code Day 13

#lang racket

(define input (file->list "d13input.txt"))

(define (convert input)
  (cond
    [(empty? input)
     empty]
    [else
     (cons (list (first input)
                 (second input))
           (convert (rest (rest input))))]))

(define coords (convert input))

(define raw-folds (file->list "d13inputfolds.txt"))

(define (threes input)
  (cond
    [(empty? (rest input))
     (list (first input))]
    [else
     (cons (first input)
           (threes (cdddr input)))]))

(define folds (threes (cddr raw-folds)))


;; Part 1:

;; performs an up fold
(define (up-fold coords y)
  (cond
    [(empty? coords)
     empty]
    [(> (second (first coords)) y)
     (cons (list (first (first coords))
                 (- y (abs (- (second (first coords)) y))))
           (up-fold (rest coords) y))]
    [else
     (cons (first coords)
           (up-fold (rest coords) y))]))

;; performs a left fold
(define (left-fold coords x)
  (cond
    [(empty? coords)
     empty]
    [(> (first (first coords)) x)
     (cons (list (- x (abs (- (first (first coords)) x)))
                 (second (first coords)))
           (left-fold (rest coords) x))]
    [else
     (cons (first coords)
           (left-fold (rest coords) x))]))

;; removes dupes from lst
(define (dedup lst)
  (foldr (lambda (x rror)
           (cons x (filter (lambda (y)
                             (not (equal? x y)))
                           rror)))
         empty lst))

(define step-one (left-fold coords 655))

;; Answer = 712
(define answer (length (dedup step-one)))



;; Part 2:

;; folds for all folds in folds
(define (keep-folding coords folds)
  (cond
    [(empty? folds)
     coords]
    [(horiz? (first folds))
     (keep-folding (left-fold coords (get-number (first folds)))
                   (rest folds))]
    [else
     (keep-folding (up-fold coords (get-number (first folds)))
                   (rest folds))]))

;; true if 'x at start
(define (horiz? fold)
  (string=? "x" (substring (symbol->string fold) 0 1)))

;; returns number of a fold instruction
(define (get-number fold)
  (local
    [(define str (symbol->string fold))]
  (string->number (substring str 2 (string-length str)))))

;; result of all folds
(define output (dedup (keep-folding coords folds)))

;; Me when i manually plot the points
;; Answer is BLHFJPJF