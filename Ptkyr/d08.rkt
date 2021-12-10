;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-lambda-reader.ss" "lang")((modname d8) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor mixed-fraction #f #t none #f () #t)))
;; Advent of Code Day 8

(require "d8input.rkt")

(define (first-line lst)
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

       (keep lst 15))]))


(define (rest-lines lst)
  (foldr (lambda (x rror)
           (rest rror))
         lst (build-list 15 +)))


(define (convert lst)
  (cond
    [(empty? lst)
     empty]
    [else
     (cons (first-line lst)
           (convert (rest-lines lst)))]))



(define signals (convert input))


;; takes in a line and outputs a list of the outputs
(define (outputs signal)
  (cond
    [(symbol=? 'x (first signal))
     (rest signal)]
    [else
     (outputs (rest signal))]))


;; returns length of symbol
(define (symbol-length sym)
  (string-length (symbol->string sym)))


;; returns true if 1, 4, 7, or 8
(define (unique-digit? n)
  (or (= 2 (symbol-length n))
      (= 3 (symbol-length n))
      (= 4 (symbol-length n))
      (= 7 (symbol-length n))))



;; returns # of 1, 4, 7, or 8
(define (count-uniques outputs)
  (foldr (lambda (x rror)
           (cond
             [(unique-digit? x)
              (+ 1 rror)]
             [else
              rror]))
         0 outputs))


;; returns total from list of signals
(define (count-all lst)
  (foldr (lambda (x rror)
           (+ (count-uniques (outputs x))
              rror))
         0 lst))

;; Answer
(check-expect (count-all signals) 543)


;; Part 2
;; takes in a line and outputs a list of the inputs
(define (inputs signal)
  (cond
    [(symbol=? 'x (first signal))
     empty]
    [else
     (cons (first signal)
           (inputs (rest signal)))]))


;; returns the element with length 2
(define (one inputs)
  (cond
    [(= 2 (symbol-length (first inputs)))
     (first inputs)]
    [else
     (one (rest inputs))]))


;; returns the element with length 3
(define (seven inputs)
  (cond
    [(= 3 (symbol-length (first inputs)))
     (first inputs)]
    [else
     (seven (rest inputs))]))


;; returns the element with length 4
(define (four inputs)
  (cond
    [(= 4 (symbol-length (first inputs)))
     (first inputs)]
    [else
     (four (rest inputs))]))


;; returns the element with length 7
(define (eight inputs)
  (cond
    [(= 7 (symbol-length (first inputs)))
     (first inputs)]
    [else
     (eight (rest inputs))]))



;; takes a symbol, returns sorted list of chars
(define (lettersort sym)
  (local
    [(define symlst (string->list (symbol->string sym)))]
    
    (quicksort symlst char<?)))


;; gets the top line in the mapping from one and seven
;; Sym Sym -> Char
(define (pos1 one seven)
  (local
    [(define yeet (lettersort one))

     (define skeet (lettersort seven))

     (define (get-top j k)
       (cond
         [(or (char=? (first k) (first j))
              (char=? (first k) (second j)))
          (get-top j (rest k))]
         [else
          (first k)]))]

    (get-top yeet skeet)))


;; returns all elements of length 5
(define (candidates inputs)
  (filter (lambda (x)
            (= 5 (symbol-length x)))
          inputs))


;; returns true if sym contains all of seven
;; Sym Sym -> Bool
(define (three? sym seven)
  (local
    [(define checks (list->string (lettersort seven)))

     (define x (substring checks 0 1))

     (define y (substring checks 1 2))

     (define z (substring checks 2 3))

     (define symstr (symbol->string sym))]

    (and (string-contains? x symstr)
         (string-contains? y symstr)
         (string-contains? z symstr))))


(define (three inputs)
  (local
    [(define possible (candidates inputs))

     (define yeet (seven inputs))]

    (first (filter (lambda (x)
                     (three? x yeet))
                   possible))))


(define (topleft one three four seven)
  (local
    [(define i (lettersort one))
     (define i1 (first i))
     (define i2 (second i))

     (define j (lettersort three))
     
     (define k (lettersort four))
     (define k1 (first k))
     (define k2 (second k))
     (define k3 (third k))
     (define k4 (fourth k))

     (define (get-cands k)
       (cond
         [(empty? k)
          empty]
         [(or (char=? (first k) i1)
              (char=? (first k) i2))
          (get-cands (rest k))]
         [else
          (cons (first k)
                (get-cands (rest k)))]))

     (define cands (get-cands k))

     (define l (lettersort seven))
     (define l1 (first l))
     (define l2 (second l))
     (define l3 (third l))

     (define top (pos1 one seven)) ; char

     (define (three-less-seven j)
       (cond
         [(empty? j)
          empty]
         [(or (char=? (first j) l1)
              (char=? (first j) l2)
              (char=? (first j) l3))
          (three-less-seven (rest j))]
         [else
          (cons (first j)
                (three-less-seven (rest j)))]))

     (define center/bottom (three-less-seven j))
     (define cb1 (first center/bottom))
     (define cb2 (second center/bottom))

     (define (get-topleft cands)
       (cond
         [(or (char=? (first cands) cb1)
              (char=? (first cands) cb2)) ; common only in center
          (second cands)]
         [else
          (first cands)]))]

    (get-topleft cands)))



(define (center one three four seven)
  (local
    [(define i (lettersort one))
     (define i1 (first i))
     (define i2 (second i))

     (define j (lettersort three))
     
     (define k (lettersort four))
     (define k1 (first k))
     (define k2 (second k))
     (define k3 (third k))
     (define k4 (fourth k))

     (define (get-cands k)
       (cond
         [(empty? k)
          empty]
         [(or (char=? (first k) i1)
              (char=? (first k) i2))
          (get-cands (rest k))]
         [else
          (cons (first k)
                (get-cands (rest k)))]))

     (define cands (get-cands k))
     (define cand1 (first cands))
     (define cand2 (second cands))

     (define l (lettersort seven))
     (define l1 (first l))
     (define l2 (second l))
     (define l3 (third l))


     (define (three-less-seven j)
       (filter (lambda (x)
            (not (or (char=? x l1)
                     (char=? x l2)
                     (char=? x l3))))
               j))

     (define center/bottom (three-less-seven j))
     (define cb1 (first center/bottom))
     (define cb2 (second center/bottom))

     (define (get-center cb)
       (cond
         [(or (char=? (first cb) cand1)
              (char=? (first cb) cand2)) ; common only in center
          (first cb)]
         [else
          (second cb)]))]

    (get-center center/bottom)))







;; true if cand has all of seven in it and center
(define (nine? cand seven center)
  (local
    [(define str (symbol->string seven))

     (define test (symbol->string cand))

     (define cen (list->string (list center)))

     (define s1 (substring str 0 1))
     (define s2 (substring str 1 2))
     (define s3 (substring str 2 3))]

    (and (string-contains? s1 test)
         (string-contains? s2 test)
         (string-contains? s3 test)
         (string-contains? cen test))))


;; true if cand contains all of five
(define (six? cand five)
  (local
    [(define str (symbol->string five))

     (define test (symbol->string cand))

     (define s1 (substring str 0 1))
     (define s2 (substring str 1 2))
     (define s3 (substring str 2 3))
     (define s4 (substring str 3 4))
     (define s5 (substring str 4 5))]

    (and (string-contains? s1 test)
         (string-contains? s2 test)
         (string-contains? s3 test)
         (string-contains? s4 test)
         (string-contains? s5 test))))


;; yeet
(define (top inputs)
  (pos1 (one inputs) (seven inputs)))



(define (get-outval signal)
  (local
    [(define ins (inputs signal))

     (define outs (outputs signal))

     (define num1 (one ins))

     (define num3 (three ins))

     (define num4 (four ins))

     (define num7 (seven ins))

     (define num8 (eight ins))

     (define 5-longs (filter (lambda (x)
                               (= 5 (symbol-length x)))
                             ins))

     (define 2-or-5 (filter (lambda (x)
                              (not (symbol=? num3 x)))
                            5-longs)) ; list of sym

     (define upleft (topleft num1 num3 num4 num7)) ; char

     (define upleftstr (list->string (list upleft)))

     (define num5lst (filter (lambda (x)
                               (string-contains? upleftstr
                                                 (symbol->string x)))
                             2-or-5))

     (define num5 (first num5lst))

     (define num2lst (filter (lambda (x)
                               (not (symbol=? num5 x)))
                             2-or-5))

     (define num2 (first num2lst))

     (define 6-longs (filter (lambda (x)
                               (= 6 (symbol-length x)))
                             ins))

     (define cen (center num1 num3 num4 num7)) ; char

     (define num9lst (filter (lambda (x)
                               (nine? x num7 cen))
                             6-longs))

     (define num9 (first num9lst))

     (define 0-or-6 (filter (lambda (x)
                              (not (symbol=? num9 x)))
                            6-longs))

     (define num6lst (filter (lambda (x)
                               (six? x num5))
                             0-or-6))

     (define num6 (first num6lst))

     (define num0lst (filter (lambda (x)
                               (not (symbol=? num6 x)))
                             0-or-6))

     (define num0 (first num0lst))

     (define (get-number sym)
       (local
         [(define test (lettersort sym))]
         (cond
           [(equal? test (lettersort num0))
            0]
           [(equal? test (lettersort num1))
            1]
           [(equal? test (lettersort num2))
            2]
           [(equal? test (lettersort num3))
            3]
           [(equal? test (lettersort num4))
            4]
           [(equal? test (lettersort num5))
            5]
           [(equal? test (lettersort num6))
            6]
           [(equal? test (lettersort num7))
            7]
           [(equal? test (lettersort num8))
            8]
           [(equal? test (lettersort num9))
            9])))]

    (map (lambda (x)
           (get-number x))
         outs)))



(define (make-num outvals)
  (+ (* 1000 (first outvals))
     (* 100 (second outvals))
     (* 10 (third outvals))
     (fourth outvals)))



(define (sum-outvals sigs)
  (foldr (lambda (x rror)
           (+ (make-num (get-outval x))
              rror))
         0 sigs))

;; Answer
(check-expect (sum-outvals signals) 994266)