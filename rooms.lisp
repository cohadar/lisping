(defvar *rooms*
  '((living-room (north front-stairs) (south dining-room) (east kitchen))
    (upstairs-bedroom (west library) (south front-stairs))
    (dining-room (north living-room) (east pantry) (west downstairs-bedroom))
    (kitchen (west living-room) (south pantry))
    (pantry (north kitchen) (west dining-room))
    (downstairs-bedroom (north back-stairs) (east dining-room))
    (back-stairs (south downstairs-bedroom) (north library))
    (front-stairs (north upstairs-bedroom) (south living-room))
    (library (east upstairs-bedroom) (south back-stairs))))

(defvar *loc* 'pantry)

(defun choices (room)
  (cdr (assoc room *rooms*)))

(defun look (direction room)
  (car (cdr (assoc direction (choices room)))))

(defun setrl (place)
  (setf *loc* place))

(defun how-many-choices ()
  (length (choices *loc*)))

(defun upstairsp ()
  (member *loc* '(upstairs-bedroom library)))



(print (upstairsp))

