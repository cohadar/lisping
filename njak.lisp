(defmacro swap (x y)
  `(progn (setf temp ,x)
         (setf ,x ,y)
         (setf ,y temp)))
