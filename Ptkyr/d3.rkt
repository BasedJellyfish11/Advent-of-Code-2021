;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-lambda-reader.ss" "lang")((modname d3) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor mixed-fraction #f #t none #f () #t)))
;; Advent of Code Day 3

(require "d3input.rkt")

;; Part 1

(define (common-bit lst pos ones zeroes)
  (cond
    [(empty? lst)
     (cond
       [(>= ones zeroes)
        1]
       [else
        0])]
    [else
     (local
       [(define test (fix-str (number->string (first lst))))]
       (cond
         [(string=? (substring test pos (add1 pos)) "1")
          (common-bit (rest lst) pos (add1 ones) zeroes)]
         [else
          (common-bit (rest lst) pos ones (add1 zeroes))]))]))


(define (output lst)
  (foldr (lambda (x rror)
           (cons (common-bit lst x 0 0)
                 rror))
         empty (build-list 12 +)))


(define (fix-str str)
  (cond
    [(= 12 (string-length str))
     str]
    [else
     (fix-str (string-append "0" str))]))


(define (bin-to-dec lst)
  (local
    [(define (func lst acc)
       (cond
         [(empty? lst)
          0]
         [else
          (+ (* (first lst) (expt 2 acc))
             (func (rest lst) (sub1 acc)))]))]

    (func lst 11)))


(define (xor lst)
  (cond
    [(empty? lst)
     empty]
    [(= 1 (first lst))
     (cons 0 (xor (rest lst)))]
    [else
     (cons 1 (xor (rest lst)))]))

(define gamma-rate (bin-to-dec (output input)))
(define epsilon-rate (bin-to-dec (xor (output input))))

;; Answer
(check-expect (* gamma-rate epsilon-rate)
              4103154)



;; Part 2
(require htdp-trace)
(define (oxygen lst acc pos)
  (local
    [(define (same-bit pos one two)
       (string=? (substring one pos (add1 pos))
                 (number->string two)))

     ;; keeps elements of lst whose pos element is num
     (define (keep pos num lst)
       (filter (lambda (x)
                 (same-bit pos (fix-str (number->string x)) num))
               lst))]

    (cond
      [(empty? (rest acc))
       acc]
      [else
       (oxygen acc (keep pos (common-bit acc pos 0 0) acc)
               (add1 pos))])))


(define (flip num)
  (cond
    [(= 1 num)
     0]
    [else
     1]))


(define (co2 lst acc pos)
  (local
    [(define (same-bit pos one two)
       (string=? (substring one pos (add1 pos))
                 (number->string two)))

     ;; keeps elements of lst whose pos element is num
     (define (keep pos num lst)
       (filter (lambda (x)
                 (same-bit pos (fix-str (number->string x)) (flip num)))
               lst))]

    (cond
      [(empty? (rest lst))
       lst]
      [else
       (co2 acc (keep pos (common-bit acc pos 0 0) acc)
               (add1 pos))])))

(define (bindec num)
  (local
    [(define (bindec/lst lst)
       (cond
         [(empty? lst)
          0]
         [(char=? #\1 (first lst))
          (+ (expt 2 (sub1 (length lst)))
             (bindec/lst (rest lst)))]
         [else
          (bindec/lst (rest lst))]))]

    (bindec/lst (string->list (number->string num)))))


(define oxygen-rating (bindec (first (oxygen input input 0))))
(define co2-rating (bindec (first (co2 input input 0))))

;; Answer
(check-expect (* oxygen-rating co2-rating)
              4245351)