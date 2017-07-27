;; Extra Scheme Questions ;;

; Q6
(define (remove item lst)
  (cond
   ((null? lst) nil)
   ((= item (car lst))(remove item (cdr lst)))
   (else (cons (car lst)
			   (remove item (cdr lst))))
   )
)


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)

; Q7
(define (composed f g)
  (lambda (x) (f (g x)))
)

; Q8
(define (max a b) (if (> a b) a b))
(define (min a b) (if (> a b) b a))

(modulo 2 3)
(modulo 0 5)

(define (gcd a b)
  (cond
   ((= b 0) a)
   (else (gcd b (modulo a b)))))

;;; Tests
(gcd 24 60)
; expect 12
(gcd 1071 462)
; expect 21

; Q9
(define (split-at lst n)
  (cond
   ((or (null? lst)
		(= 0 n)) (cons nil lst))
   (else (cons (append
				(list (car lst))
				(car (split-at (cdr lst) (- n  1))))				
			   (cdr (split-at (cdr lst) (- n  1))))
   )))

(split-at '(1 2 3 4 5) 3)
