;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-lambda-reader.ss" "lang")((modname d4) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor mixed-fraction #f #t none #f () #t)))
;; Advent of Code Day 4

(require "d4input.rkt")

;; Part 1:
;; A Board is a (listof Nat)
;;   Requires: all elements are unique, length = 25
(define mark 'yeet)

;; (next-board lst) takes (rest lst) 25 times
;; next-board: (listof Any) -> (listof Any)
;;   Requires: (length lst) == 0 (mod 25)
(define (next-board lst)
  (foldr (lambda (x rror)
           (rest rror))
         lst (build-list 25 +)))


;; (first-board lst) takes the first 25 elements of lst
;; first-board: (listof Any) -> (listof Any)
;;   Requires: (length lst) >= 25
(define (first-board lst)
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

       (keep lst 25))]))



(define (convert lst)
  (cond
    [(empty? lst)
     empty]
    [else
     (cons (first-board lst)
           (convert (next-board lst)))]))



;; (win? board) produces true if board is a winning board, false otherwise
;; win: Board -> Bool
(define (win? board)
  (local
    [(define (horiz-win? board)
       (cond
         [(empty? board)
          false]
         [else
          (or (and (equal? mark (first board))
                   (equal? mark (second board))
                   (equal? mark (third board))
                   (equal? mark (fourth board))
                   (equal? mark (fifth board)))
              (horiz-win? (next-row board)))]))

     (define (vert-win? board)
       (local
         [;; produces true if all mod 5 = n positions are marked
          (define (vert-win board n)
            (cond
              [(empty? board)
               false]
              [(= n (remainder (length board) 5))
               (cond
                 [(equal? mark (first board))
                  (cond
                    [(>= 5 (length board))
                     true]
                    [else
                     (vert-win (rest board) n)])]
                 [else
                  false])]
              [else
               (vert-win (rest board) n)]))]

         (foldr (lambda (x rror)
                  (or (vert-win board x)
                      rror))
                false (build-list 5 +))))]

    (or (horiz-win? board)
        (vert-win? board))))



;; takes (rest lst) 5 times
(define (next-row board)
  (foldr (lambda (x rror)
           (rest rror))
         board (build-list 5 +)))



;; replaces occurrences of n with mark
(define (mark-off board n)
  (foldr (lambda (x rror)
           (cond
             [(equal? n x)
              (cons mark rror)]
             [else
              (cons x rror)]))
         empty board))



(define (score board)
  (foldr (lambda (x rror)
           (cond
             [(equal? mark x)
              rror]
             [else
              (+ x rror)]))
         0 board))


;; produces score of winning board if win and false otherwise
(define (board-win? lst)
  (cond
    [(empty? lst)
     false]
    [(win? (first lst))
     (score (first lst))]
    [else
     (board-win? (rest lst))]))



(define (cross-off lst n)
  (cond
    [(empty? lst)
     empty]
    [else
     (cons (mark-off (first lst) n)
           (cross-off (rest lst) n))]))


(define input (convert boards))
;; main function
(define (bingo lst nums)
  (local
    [(define current (first nums))
     (define next-round (cross-off lst current))
     (define result (board-win? next-round))]
    (cond
      [(false? result)
       (bingo next-round (rest nums))]
      [else
       (* result current)])))

;; Answer
(check-expect (bingo input draw) 8580)



;; Part 2

(define (all-win? lob)
  (cond
    [(empty? lob)
     true]
    [else
     (and (win? (first lob))
          (all-win? (rest lob)))]))



(define (find-loser lob)
  (cond
    [(empty? lob)
     false]
    [(win? (first lob))
     (find-loser (rest lob))]
    [else
     (first lob)]))



(define (last lst nums)
  (local
    [(define current (first nums))
     (define next-round (cross-off lst current))
     (define result (all-win? next-round))]
    (cond
      [(false? result)
       (last next-round (rest nums))]
      [else
       (* current (score (mark-off (find-loser lst) current)))])))

;; Answer
(check-expect (last input draw) 9576)