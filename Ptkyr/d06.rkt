;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-lambda-reader.ss" "lang")((modname d6) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor mixed-fraction #f #t none #f () #t)))
;; Advent of Code Day 6

(require "d6input.rkt")

;; Part 1

;; produces # fish after days
(define (fish-after start days)
  (local
    [;; makes a one day interation
     (define (one-day lst)
       (cond
         [(empty? lst)
          empty]
         [(= 0 (first lst))
          (cons 6 (cons 8
                        (one-day (rest lst))))]
         [else
          (cons (sub1 (first lst))
                (one-day (rest lst)))]))]
    
    (cond
      [(= 0 days)
       (length start)]
      [else
       (fish-after (one-day start) (sub1 days))])))

;; Answer
(check-expect (fish-count (fish-age input) 80) 362346)


;; Part 2

;; produces the number of fish with each age
(define (fish-age fish)
  (local
    [;; helper with acc list
     (define (ages lst acc)
       (cond
         [(empty? lst)
          acc]
         [else
          (ages (rest lst) (add-age (first lst) acc))]))]

    (ages fish (build-list 9 (lambda (x)
                               0)))))


(define (add-age n ages)
  (cond
    [(empty? ages)
     empty]
    [(= 0 n)
     (cons (add1 (first ages))
           (add-age (sub1 n) (rest ages)))]
    [else
     (cons (first ages)
           (add-age (sub1 n) (rest ages)))]))


(define (shift lst)
  (append (rest lst) (list (first lst))))



(define (age-iter age-list)
  (local
    [(define sex (first age-list))

     ;; add to the 6th element
     (define (add6 n lst)
       (foldr (lambda (x rror)
                (cond
                  [(= 2 (length rror))
                   (cons (+ x n) rror)]
                  [else
                   (cons x rror)]))
              empty lst))]

    (add6 sex (shift age-list))))


(define (fish-count age-count days)
  (cond
    [(= days 0)
     (foldr (lambda (x rror)
              (+ x rror))
            0 age-count)]
    [else
     (fish-count (age-iter age-count) (sub1 days))]))

;; Answer
(check-expect (fish-count (fish-age input) 256) 1639643057051)