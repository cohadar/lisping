(defun ror (l)
  (let ((njak (reverse (rest (reverse l)))))
    (cons (car (last l)) njak)))

(print (ror '(a b c d e )))


