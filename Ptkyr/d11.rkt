;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-lambda-reader.ss" "lang")((modname d11) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor mixed-fraction #f #t none #f () #t)))
;; Advent of Code Day 11

(require "d11input.rkt")

;; Part 1:
(define (first-line lst)
  (string->list (first lst)))


(define (convert lst)
  (cond
    [(empty? lst)
     empty]
    [else
     (cons (first-line lst)
           (convert (rest lst)))]))

(define scuffed (convert input))


(define (to-num lst)
  (cond
    [(empty? lst)
     empty]
    [(char=? #\newline (first lst))
     (to-num (rest lst))]
    [else
     (cons (- (char->integer (first lst)) 48)
           (to-num (rest lst)))]))
     
;; all this work to get a list of numbers
(define better (to-num (first scuffed)))


(define (add-assoc num alst)
  (cond
    [(empty? alst)
     (list (list num 1))]
    [else
     (cons (first alst)
           (add-assoc num (rest alst)))]))


;; assoc list of indices and energy levels (initial, all are 1)
(define thing (foldl (lambda (x rror)
                       (add-assoc x rror))
                     empty (build-list 100 +)))


;; replaces val of k in alst, does nothing if k not in alst
(define (assoc-replace k v alst)
  (cond
    [(empty? alst)
     empty]
    [(= k (key (first alst)))
     (cons (list k v)
           (rest alst))]
    [else
     (cons (first alst)
           (assoc-replace k v (rest alst)))]))


(define (key pair)
  (first pair))

(define (val pair)
  (second pair))


;; just to set up initial array
(define (initial input n alst)
  (cond
    [(empty? input)
     alst]
    [else
     (initial (rest input) (add1 n)
              (assoc-replace n (first input) alst))]))


;; real input
(define array (initial better 0 thing))
(define example-array (initial (to-num (first (convert example))) 0 thing))

;; each key in adj has 1 added to its val in alst
(define (update adj alst)
  (cond
    [(empty? adj)
     alst]
    [else
     (update (rest adj)
             (assoc-update (first adj) alst))]))


;; replaces raises val of v by 1
(define (assoc-update k alst)
  (cond
    [(empty? alst)
     empty]
    [(= k (key (first alst)))
     (cons (list k (add1 (val (first alst))))
           (rest alst))]
    [else
     (cons (first alst)
           (assoc-update k (rest alst)))]))


(define (adj-list n)
  (cond
    [(= 0 (remainder n 10)) ; left edge
     (list (- n 10)   ; up
           (- n 9)    ; up right
           (+ n 1)    ; right
           (+ n 10)   ; down
           (+ n 11))] ; down right
    [(= 9 (remainder n 10)) ; right edge
     (list (- n 11)   ; upleft
           (- n 10)   ; up
           (- n 1)    ; left
           (+ n 9)    ; down left
           (+ n 10))] ; down
    [else
     (list (- n 11)   ; upleft
           (- n 10)   ; up
           (- n 9)    ; up right
           (- n 1)    ; left
           (+ n 1)    ; right
           (+ n 9)    ; down left
           (+ n 10)   ; down
           (+ n 11))])) ; down right


; counts how many keys have vals > 9
(define (flashcount alst)
  (local
    [(define (flashcount/acc alst count)
       (cond
         [(empty? alst)
          count]
         [(< 9 (val (first alst)))
          (flashcount/acc (rest alst) (add1 count))]
         [else
          (flashcount/acc (rest alst) count)]))]

    (flashcount/acc alst 0)))


;; replaces all vals > 9 with 0
(define (octopus-tame alst)
  (cond
    [(empty? alst)
     empty]
    [(< 9 (val (first alst)))
     (cons (list (key (first alst)) 0)
           (octopus-tame (rest alst)))]
    [else
     (cons (first alst)
           (octopus-tame (rest alst)))]))


;; adds 1 to each val in alst
(define (update-all alst)
  (update (build-list 100 +) alst))


;; adds 1 to the vals of each adj to key in alst
(define (flash key alst)
  (update (adj-list key) alst))



;; makes things flash, reclst = alst initially and each
;;   key in the lst flashes if its val > 9 and its key not in flashed-keys
(define (anyflashers reclst alst flashed-keys)
  (cond
    [(empty? reclst)
     (list alst flashed-keys)]
    [(member? (key (first reclst)) flashed-keys)
     (anyflashers (rest reclst) alst flashed-keys)]
    [(< 9 (val (first reclst)))
     (anyflashers (rest reclst)
                  (flash (key (first reclst)) alst)
                  (cons (key (first reclst)) flashed-keys))]
    [else
     (anyflashers (rest reclst) alst flashed-keys)]))


;; we need to cascade flashes
(define (keepflashing alst all-flashed)
  (local
    [(define baseflash (flashcount alst))

     (define result (anyflashers alst alst all-flashed))

     (define new-array (first result))

     (define res-count (flashcount new-array))

     (define flashed (second result))]

    (cond
      [(equal? baseflash res-count)
       new-array]
      [else
       (keepflashing new-array flashed)])))


;; one step of the octopus schmooves
(define (iteration alst)
  (keepflashing (update-all alst) empty))


;; sum of flash iterations
(define (all-flash n alst)
  (cond
    [(= n 0)
     0]
    [else
     (local
       [(define new (iteration alst))]
       (+ (flashcount new)
          (all-flash (sub1 n) (octopus-tame new))))]))

;; Answer
(check-expect (all-flash 100 array) 1729)



;; Part 2:
;; initialize n to 1 counts correctly
(define (until-all n alst)
  (local
    [(define new (iteration alst))]

    (cond
      [(= 100 (flashcount new))
       n]
      [else
       (until-all (add1 n) (octopus-tame new))])))

;; Answer
(check-expect (until-all 1 array) 237)