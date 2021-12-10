;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-lambda-reader.ss" "lang")((modname d10) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor mixed-fraction #f #t none #f () #t)))
;; Advent of Code Day 10

(require "d10input.rkt")

(define huh (string->list (first input)))

(require htdp-trace)

(define (first-line input)
  (cond
    [(empty? input)
     empty]
    [(char=? #\newline (first input))
     empty]
    [else
     (cons (first input)
           (first-line (rest input)))]))


(define (rest-lines input)
  (cond
    [(empty? input)
     empty]
    [(char=? #\newline (first input))
     (rest input)]
    [else
     (rest-lines (rest input))]))


(define (convert input)
  (cond
    [(empty? input)
     empty]
    [else
     (cons (first-line input)
           (convert (rest-lines input)))]))


(define listinput (convert huh))

(define parenscore 3)

(define bracketscore 57)

(define bracescore 1197)

(define greatscore 25137)


;; return closing of given opening char
(define (closer char)
  (cond
    [(char=? #\( char)
     #\)]
    [(char=? #\[ char)
     #\]]
    [(char=? #\{ char)
     #\}]
    [(char=? #\< char)
     #\>]))


;; returns score
(define (score char)
  (cond
    [(char=? #\) char)
     parenscore]
    [(char=? #\] char)
     bracketscore]
    [(char=? #\} char)
     bracescore]
    [(char=? #\> char)
     greatscore]))


;; returns true if open char, false otherwise
(define (open-char? char)
  (or (char=? #\( char)
      (char=? #\[ char)
      (char=? #\{ char)
      (char=? #\< char)))


;; returns true if close char, false otherwise
(define (close-char? char)
  (or (char=? #\) char)
      (char=? #\] char)
      (char=? #\} char)
      (char=? #\> char)))


;; returns if valid thing, returns score if invalid
(define (corrupt chunk)
  (cond
    [(empty? chunk)
     empty]
    [else
     (local
       [;; acc contains previous elements
        (define (corrupt? chunk acc)
          (cond
            [(empty? chunk)
             acc]
            [(open-char? (first chunk))
             (corrupt? (rest chunk) (cons (first chunk) acc))]
            [(char=? (closer (first acc)) (first chunk))
             (corrupt? (rest chunk) (rest acc))]
            [else
             (score (first chunk))]))]

       (corrupt? chunk empty))]))



;; product of errors in input list
(define (errors lst score)
  (cond
    [(empty? lst)
     score]
    [else
     (local
       [(define result (corrupt (first lst)))]
       (cond
         [(number? result)
          (errors (rest lst) (+ result score))]
         [else
          (errors (rest lst) score)]))]))

;; Answer
(check-expect (errors listinput 0) 374061)



;; Part 2
(define incompletes (filter (lambda (x)
                              (not (number? (corrupt x))))
                            listinput))


;; turns list of opens to list of closers
(define (open-to-close lst)
  (map (lambda (x)
         (closer x))
       lst))


;; takes score of list of completers
(define (score-complete acc score)
  (cond
    [(empty? acc)
     score]
    [else
     (score-complete (rest acc)
                     (+ (* 5 score) (two-score (first acc))))]))


;; returns score of char
(define (two-score char)
  (cond
    [(char=? #\) char)
     1]
    [(char=? #\] char)
     2]
    [(char=? #\} char)
     3]
    [(char=? #\> char)
     4]))


(define accs (map (lambda (x)
                    (corrupt x))
                  incompletes))

(define scores (map (lambda (x)
                      (score-complete (open-to-close x) 0))
                    accs))

(define sorted (quicksort scores >))

(define n (/ (length sorted) 2))

(define/trace (get-median lst index)
  (cond
    [(<= index 1)
     (first lst)]
    [else
     (get-median (rest lst) (sub1 index))]))

;; Answer
(check-expect (get-median sorted n) 2116639949)