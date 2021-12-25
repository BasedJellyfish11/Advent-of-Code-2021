#lang racket

;; Advent of Code Day 17

(define target-area '(248 285 -85 -56))

(define left-edge (first target-area))
(define right-edge (second target-area))
(define bottom-edge (third target-area))
(define top-edge (fourth target-area))

;; Part 1:

;; produces list of all points hit for a given success
;;  and false if fails
(define (hit x-pos y-pos x-vel y-vel)
  (cond
    [(< y-pos bottom-edge)
     false]
    [(and (<= left-edge x-pos right-edge)
          (<= bottom-edge y-pos top-edge))
     empty]
    [(= 0 x-vel)
     (cons (list x-pos y-pos)
           (hit x-pos (+ y-pos y-vel) x-vel (sub1 y-vel)))]
    [else
     (cons (list x-pos y-pos)
           (hit (+ x-pos x-vel) (+ y-pos y-vel)
                (sub1 x-vel) (sub1 y-vel)))]))



;; by inspection max occurs when y-vel = 84
(define all-points (hit 0 0 23 84))

;; take last to get answer
(define sorted-points (sort all-points  #:key second <))


;; Part 2

;; produces true if x-vel y-vel produces an x-pos y-pos
;;   within target-area and false otherwise
(define (hit? x-pos y-pos x-vel y-vel)
  (cond
    [(< y-pos bottom-edge)
     false]
    [(and (<= left-edge x-pos right-edge)
          (<= bottom-edge y-pos top-edge))
     true]
    [(= 0 x-vel)
     (hit? x-pos (+ y-pos y-vel) x-vel (sub1 y-vel))]
    [else
     (hit? (+ x-pos x-vel) (+ y-pos y-vel)
           (sub1 x-vel) (sub1 y-vel))]))


;; by the gaussian sum we only hit if x-vel = 22 or 23 and y-vel > 0
(define check22 (foldr (lambda (y rror)
                         (cons (list y (hit? 0 0 22 y))
                               rror))
                       empty (build-list 1000 add1)))

(define check23 (foldr (lambda (y rror)
                         (cons (list y (hit? 0 0 23 y))
                               rror))
                       empty (build-list 1000 add1)))


(define valid22 (filter (lambda (x)
                          (boolean=? true (second x)))
                        check22))

(define valid23 (filter (lambda (x)
                          (boolean=? true (second x)))
                        check23))


(define (count-x x-vel)
  (length (filter (lambda (x)
                    (boolean=? true (second x)))
                  (foldr (lambda (y rror)
                           (cons (list y (hit? 0 0 x-vel y))
                                 rror))
                         empty (build-list 100 add1)))))

(define (count-all-x lst)
  (cond
    [(empty? lst)
     0]
    [else
     (+ (count-x (first lst))
        (count-all-x (rest lst)))]))
                        

;; the valid velocities for y-vel > 0
;;   this is actually a lie but whatever
(define y>0 (+ (length valid22) (length valid23)))

;; produces how many y-vels in lst work for each
;;   x-vel from 0 to 286
(define (count-all lst)
  (cond
    [(empty? lst)
     0]
    [else
     (+ (length (filter (lambda (x)
                          (boolean=? true (second x)))
                        (foldr (lambda (x rror)
                                 (cons (list x (hit? 0 0 x (first lst)))
                                       rror))
                               empty (build-list (add1 right-edge) add1))))
        (count-all (rest lst)))]))

;; consider all y-vels from 0 to -85
(define yeet (count-all
              (build-list (add1 (abs bottom-edge)) (lambda (x)
                                                     (- x)))))

;; lmao arbitrarily chosen limit for x velocities
(define p2ans (count-all-x (build-list 80 +)) yeet)