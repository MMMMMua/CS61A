; Scheme

(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cddr s))
)

(define (sign x)
  (cond
   ((> x 0) 1)
   ((= x 0) 0)
   ((< x 0) -1)
   ))

(define (ordered? s)
  (cond
   ((or
	 (null? s)
	 (null? (cdr s))
	 ) #t)
   ((not (> (car s) (cadr s))) (ordered? (cdr s)))
   (else #f)
))

(define (nodots s)
  (cond
   ((or (null? s) (number? s)) s)
   ((number? (cdr s)) (list (nodots (car s))
							(cdr s)))
   (else (append (list (nodots (car s)))
			   (nodots (cdr s))))))
			
; Sets as sorted lists

(define (empty? s) (null? s))

(define (contains? s v)
    (cond ((empty? s) #f)
          ((= v (car s)) #t)
		  (else (contains? (cdr s) v))
          ))

; Equivalent Python code, for your reference:
;
; def empty(s):
;     return s is Link.empty
;
; def contains(s, v):
;     if empty(s):
;         return False
;     elif s.first > v:
;         return False
;     elif s.first == v:
;         return True
;     else:
;         return contains(s.rest, v)

(define (add s v)
    (cond ((empty? s) (list v))
          ((= v (car s)) s)
		  ((> v (car s)) (cons
						  (car s)
						  (add (cdr s) v)))
		  (else (cons v	s))
          ))

(define (intersect s t)
    (cond ((or (empty? s) (empty? t)) nil)
		  ((= (car s) (car t)) (cons (car s) (intersect (cdr s) t)))
		  ((< (car s) (car t)) (intersect (cdr s) t))
		  ((> (car s) (car t)) (intersect s (cdr t)))
		  ))

; Equivalent Python code, for your reference:
;
; def intersect(set1, set2):
;     if empty(set1) or empty(set2):
;         return Link.empty
;     else:
;         e1, e2 = set1.first, set2.first
;         if e1 == e2:
;             return Link(e1, intersect(set1.rest, set2.rest))
;         elif e1 < e2:
;             return intersect(set1.rest, set2)
;         elif e2 < e1:
;             return intersect(set1, set2.rest)

(define (union s t)
    (cond ((empty? s) t)
          ((empty? t) s)
		  ((= (car s)
			  (car t))
		   (cons (car s)
				 (union (cdr s)
						(cdr t))))
		  ((< (car s)
			  (car t)) (cons (car s)
							 (union (cdr s)
									t)))
		  (else (cons (car t)
					  (union s
							 (cdr t))))
		  ))

; Tail-Calls in Scheme

(define (exp-recursive b n)
  (if (= n 0)
      1
      (* b (exp-recursive b (- n 1)))))

(define (exp b n)
  ;; Computes b^n.
  ;; b is any number, n must be a non-negative integer.
  (define (helper n res)
	(if (= n 0) res
		(helper (- n 1) (* res b))))
  (helper n 1))


(define (filter pred lst)
  (define (helper lst res)
	(cond
	 ((null? lst) res)
	 ((pred (car lst)) (helper (cdr lst)
							   (append res
									   (list (car lst)))))
	 (else (helper (cdr lst)
	 			   res))))
  (helper lst ()))

(define (even? x)
  (= (modulo x 2) 0))

(filter even? '(2 4 6))
