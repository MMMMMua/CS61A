(define (reverse0 lst)
  (cond
   ((null? lst) lst)
   (else (append (reverse0 (cdr lst))
				 (list (car lst))))))

(define (reverse1 lst)
  (define (helper lst rev)
	(cond
	 ((null? lst) rev)
	 (else (helper (cdr lst)
				   (cons (car lst)
						 rev)))))
  (helper lst nil))

(reverse0 '(1 2 3))
(reverse1 '(1 2 3 4 5 6 7))
