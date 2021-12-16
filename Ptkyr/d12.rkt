;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-lambda-reader.ss" "lang")((modname d12) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor mixed-fraction #f #t none #f () #t)))
;; Advent of Code Day 12

(require "d12input.rkt")

(require htdp-trace)

;; Sym -> (list Sym Sym)
(define (split connection)
  (local
    [(define lst (string->list (symbol->string connection)))

     (define (return-first lst)
       (cond
         [(char=? #\- (first lst))
          empty]
         [else
          (cons (first lst)
                (return-first (rest lst)))]))

     (define (return-last lst)
       (cond
         [(char=? #\- (first lst))
          (rest lst)]
         [else
          (return-last (rest lst))]))]

    (list (list->string (return-first lst))
          (list->string (return-last lst)))))

;; (list Node Node) Graph -> Graph
(define (add-graph node graph)
  (cond
    [(empty? graph)
     (list (list (first node) (list (second node))))]
    [(string=? (first node) (vertex (first graph)))
     (cons (list (vertex (first graph))
                 (cons (second node) (nbrs (first graph))))
           (rest graph))]
    [else
     (cons (first graph)
           (add-graph node (rest graph)))]))


(define (vertex node)
  (first node))


(define (nbrs node)
  (second node))


(define (switch node)
  (list (second node) (first node)))


(define splits (foldr (lambda (x rror)
                        (cons (split x)
                              rror))
                      empty input))

(define graph (foldr (lambda (x rror)
                       (add-graph x rror))
                     empty splits))

;; Actual useful input, undirected graph
(define caves (foldr (lambda (x rror)
                       (add-graph (switch x) rror))
                     graph splits))



;; Part 1:

;; better named built-in function
(define (smallcave? cave)
  (string-lower-case? cave))


;; returns number of paths from start to end
(define (all-paths graph)
  (path/node "start" graph empty))


;; returns how many paths there are from start to end
(define (path/node start graph smalls)
  (cond
    [(string=? "end" start)
     1]
    [(smallcave? start)
     (path/nbrs (outnbrs start graph)
                graph (cons start smalls))]
    [else
     (path/nbrs (outnbrs start graph)
                graph smalls)]))


;; returns the number of paths there are from all nodes in lst to end
(define (path/nbrs lst graph smalls)
  (cond
    [(empty? lst)
     0]
    [(member? (first lst) smalls)
     (path/nbrs (rest lst) graph smalls)]
    [else
     (+ (path/node (first lst) graph smalls)
        (path/nbrs (rest lst) graph smalls))]))


;; returns nbrs of node in graph
(define (outnbrs node graph)
  (cond
    [(string=? node (vertex (first graph)))
     (nbrs (first graph))]
    [else
     (outnbrs node (rest graph))]))

;; Answer
(check-expect (all-paths caves) 5874)



;; Part 2

;; returns true if lst has a duplicate element
(define (revisited? lst)
  (cond
    [(empty? lst)
     false]
    [(member? (first lst) (rest lst))
     true]
    [else
     (revisited? (rest lst))]))


;; returns number of paths from start to end
(define (all-paths2 graph)
  (path/node2 "start" graph empty))


;; returns how many paths there are from start to end
(define (path/node2 start graph smalls)
  (cond
    [(string=? "end" start)
     1]
    [(smallcave? start)
     (path/nbrs2 (outnbrs start graph)
                 graph (cons start smalls))]
    [else
     (path/nbrs2 (outnbrs start graph)
                 graph smalls)]))


;; returns the number of paths there are from all nodes in lst to end
(define (path/nbrs2 lst graph smalls)
  (cond
    [(empty? lst)
     0]
    [(string=? "start" (first lst))
     (path/nbrs2 (rest lst) graph smalls)]
    [(and (member? (first lst) smalls)
          (revisited? smalls))
     (path/nbrs2 (rest lst) graph smalls)]
    [else
     (+ (path/node2 (first lst) graph smalls)
        (path/nbrs2 (rest lst) graph smalls))]))

;; Answer
(check-expect (all-paths2 caves) 153592)