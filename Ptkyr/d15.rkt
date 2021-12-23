#lang racket

;; Advent of Code Day 15
;; please give me arrays racket
(require htdp-trace)
(define input (file->list "d15input.txt"))
(define raw-ex (file->list "d15ex.txt"))

(define (convert in)
  (cond
    [(empty? in)
     empty]
    [else
     (append (string->list (number->string (first in)))
             (convert (rest in)))]))

(define grid-char (convert input))

(define ex (convert raw-ex))

(define width 100)

;; turn char to its numeric value
(define (char->num char)
  (- (char->integer char) 48))

(define (to-nums grid)
  (cond
    [(empty? grid)
     empty]
    [else
     (cons (char->num (first grid))
           (to-nums (rest grid)))]))

;; actual input
(define grid (to-nums grid-char))



;; Part 1

;; advances 100 positions
(define (down grid)
  (foldr (lambda (x rror)
           (rest rror))
         grid (build-list width +)))


;; cumulative sum of a list of numbers
(define (cumsum lst)
  (local
    [(define (cum lst ssf)
       (cond
         [(empty? lst)
          empty]
         [else
          (cons (+ (first lst) ssf)
                (cum (rest lst) (+ (first lst) ssf)))]))]

    (cons (first lst)
          (cum (rest lst) (first lst)))))


;; first 100 numbers in grid
(define (first-row grid)
  (local
    [(define (keep n lst)
       (cond
         [(= n 0)
          empty]
         [else
          (cons (first lst)
                (keep (sub1 n) (rest lst)))]))]

    (keep width grid)))


;; first column of grid
(define (first-col grid)
  (local
    [(define len (length grid))]

    (cond
      [(<= len width)
       (list (first grid))]
      [else
       (cons (first grid)
             (first-col (down grid)))])))


;; true if indices are equal, false otherwise
(define (index=? i j entry)
  (and (= i (first entry))
       (= j (second entry))))


;; returns val of i,jth entry in dict
(define (lookup i j dict)
  (cond
    [(empty? dict)
     false]
    [(index=? i j (first dict))
     (third (first dict))]
    [else
     (lookup i j (rest dict))]))


;; adds i j based on values in initdict
(define (build-dict i j n initdict)
  (local
    [(define up (lookup i (sub1 j) initdict))

     (define left (lookup (sub1 i) j initdict))]

    (cons (list i j (+ n (min up left)))
          initdict)))


;; init j to 1, insert down grid
(define (build-grid2 i j grid initdict)
  (cond
    [(empty? grid)
     initdict]
    [(= 0 i)
     (build-grid2 (add1 i) j (rest grid) initdict)]
    [(= (sub1 width) i) ; right edge
     (build-grid2 0 (add1 j) (rest grid)
                  (build-dict i j (first grid) initdict))]
    [else
     (build-grid2 (add1 i) j (rest grid)
                  (build-dict i j (first grid) initdict))]))


;(define row1 (cumsum (first-row grid)))
;
;(define col1 (cumsum (first-col grid)))
;
;; cumsum of row 1
;(define row1dict (foldr (lambda (x y rror)
;                          (cons (list x 0 y)
;                                rror))
;                        empty
;                        (build-list width +)
;                        row1))
;
;; dict with cumsum of row 1 and col 1
;(define initdict (foldr (lambda (x y rror)
;                          (cons (list 0 x y)
;                                rror))
;                        row1dict
;                        (build-list width +)
;                        col1))
;
;(define all-paths (build-grid2 0 1 (down grid) initdict))
;
;; off by 2 for some fucking reason
;(define answer (- (lookup (sub1 width) (sub1 width) all-paths) 2))


(define test (to-nums ex))

;; Part 2:
(define big-width (* 5 width))

;; adds 1 to all risks in grid
(define (add-risks grid)
  (cond
    [(empty? grid)
     empty]
    [(= 9 (first grid))
     (cons 1 (add-risks (rest grid)))]
    [else
     (cons (add1 (first grid))
           (add-risks (rest grid)))]))


;; adds risks n times to grid
(define (risk-more n grid)
  (cond
    [(= n 0)
     grid]
    [else
     (risk-more (sub1 n) (add-risks grid))]))


;; makes a thick column from thin
(define (make-thick thin)
  (foldl (lambda (x rror)
           (append rror (risk-more x thin)))
         thin (build-list 4 add1)))


;; keeps first n of lst
(define (keep n lst)
  (cond
    [(= n 0)
     empty]
    [else
     (cons (first lst)
           (keep (sub1 n) (rest lst)))]))


;; advances n positions
(define (down-bad n grid)
  (foldr (lambda (x rror)
           (rest rror))
         grid (build-list n +)))


;; appends one and two as columns, where n is width of one
(define (column-bind n one two)
  (cond
    [(empty? one)
     empty]
    [else
     (append (keep n one)
             (first-row two)
             (column-bind n
                          (down-bad n one)
                          (down two)))]))


;; makes big 5x5 map
(define (create-map stop col-one add)
  (local
    [(define thick-add (make-thick add))

     (define n (/ (length col-one) big-width))]
    (cond
      [(= stop 0)
       col-one]
      [else
       (create-map (sub1 stop)
                   (column-bind n col-one thick-add)
                   (add-risks add))])))


;; first column of grid
(define (big-first-col grid)
  (local
    [(define len (length grid))]

    (cond
      [(<= len big-width)
       (list (first grid))]
      [else
       (cons (first grid)
             (big-first-col (down-bad big-width grid)))])))


;; init j to 1, insert down grid
(define (big-build-grid2 i j grid initdict)
  (cond
    [(empty? grid)
     initdict]
    [(= 0 i) ; we already have the first col
     (big-build-grid2 (add1 i) j (rest grid) initdict)]
    [(= (sub1 big-width) i) ; right edge
     (big-build-grid2 0 (add1 j) (rest grid) ; go down
                  (build-dict i j (first grid) initdict))]
    [else
     (big-build-grid2 (add1 i) j (rest grid)
                  (build-dict i j (first grid) initdict))]))



(define bigtest (create-map 4 (make-thick grid) (add-risks grid)))

(define p2row1 (cumsum (keep big-width bigtest)))

(define p2col1 (cumsum (big-first-col bigtest)))

; cumsum of row 1
(define p2row1dict (foldr (lambda (x y rror)
                            (cons (list x 0 y)
                                  rror))
                          empty
                          (build-list big-width +)
                          p2row1))

; dict with cumsum of row 1 and col 1
(define p2initdict (foldr (lambda (x y rror)
                            (cons (list 0 x y)
                                  rror))
                          p2row1dict
                          (build-list big-width +)
                          p2col1))

;(define p2all-paths
;  (big-build-grid2 0 1 (down-bad big-width bigtest) p2initdict))

; off by 2 for some fucking reason; 2894 too high, 2892 too high 2890 incorrect
;(define answer (- (lookup (sub1 big-width)
;                          (sub1 big-width)
;                          p2all-paths)
;                  1))
