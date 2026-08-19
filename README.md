# Estructura-de-Datos-Con-Petes
creado por emi no esperen mucho
Paso a paso que hacer al trabajar
Primero: pulleamos el main no vaya a ser que alguien haya subido algo

=======

Guia de comandos rapida
Antes de empezar, pulleamos el main.

git checkout main
git pull origin main
Creamos la branch, por si no lo hicimos todavia

git checkout -b nombre-de-tu-branch
Con un git branch chequeas que estes donde tenes que estar
Ahora vinculas la branch con lo que tenes vos. Pueden tener una carpeta con la branch suya y otro con el main si quieren.

git push -u origin nombre-de-tu-branch
A partir de donde hagamos ese codigo, cada push que hagas se hace en tu branch.
Si modifican el main y queres traer los cambios usamos

git checkout main
git pull origin main
git checkout nombre-de-tu-branch
git merge main
Resumen rapido
git checkout main
git pull origin main
git checkout -b mi-branch
git add .
git commit -m "Descripción del cambio"
git push -u origin mi-branch
Creamos cada uno nuestra rama con nuestor nombre

git checkout -b nombre-de-tu-rama
Si nuestra rama ya existe usas el comando de arriba sin -b Sino tambien podes usar git switch nombre-de-la-rama
Chequeas en cual rama estas trabajando con git branch. La rama activa a parece con un asterisco
Una vez que haces el add y el commit, usas este push

git push -u origin nombre-de-tu-rama
El u hace que a partir de ahora cuando hagas algun push, pushee directamente en la rama. \

Entonces, cada vez que arrancas:

git checkout nombre-de-tu-rama
git pull origin nombre-de-tu-rama
