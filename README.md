# Estructura de Datos Con Petes 
# Para nada este README fue copiado de protocolos
Repositorio usado para la asignatura de "Estructura de Datos" dictada en la UCA 
### Como trabajamos?
Hagamos asi, tengamos cada uno de nosotros nuestra propia branch. Trabajemos sobre nuestras branches y cuando tengamos algo lo pusheamos a la main, asi no tenemos que andar quejandonos con conflictos.
## En palabras de LOL cada uno por su linea y esperar los ganks

### Como organizamos los archivos?.
### Igual que como te compras los items en la tienda, igual de ordenadito
Hagamos lo siguiente: las carpetas que vamos a tener que saen TP1/TP2/...  

---
### Paso a paso que hacer al trabajar, BASICAMENTE pegarle al nexo para ganar
## Santi esto es para vos
Primero: pulleamos el main no vaya a ser que alguien haya subido algo 

=======
### Guia de comandos rapida, Como una casual con bots
Antes de empezar, pulleamos el main.
```bash
git checkout main
git pull origin main
```

Creamos la branch, por si no lo hicimos todavia
```bash
git checkout -b nombre-de-tu-branch ejemplo fan de irelia
```
Con un `git branch` chequeas que estes donde tenes que estar \
Ahora vinculas la branch con lo que tenes vos. Pueden tener una carpeta con la branch suya y otro con el main si quieren.
```bash
git push -u origin nombre-de-tu-branch
```

A partir de donde hagamos ese codigo, cada push que hagas se hace en tu branch.\
Si modifican el main y queres traer los cambios usamos
```bash
git checkout main
git pull origin main
git checkout nombre-de-tu-branch
git merge main
```
---
### Resumen rapido, Como una Partida contra un Locke 10/0
```bash
git checkout main
git pull origin main
git checkout -b mi-branch
git add .
git commit -m "Descripción del cambio por ejemplo smolder LPM"
git push -u origin mi-branch
```
Creamos cada uno nuestra rama con nuestor nombre
```bash
git checkout -b nombre-de-tu-rama
```
Si nuestra rama ya existe usas el comando de arriba sin `-b` 
Sino tambien podes usar `git switch nombre-de-la-rama` \
Chequeas en cual rama estas trabajando con `git branch`. La rama activa a parece con un asterisco \
Una vez que haces el add y el commit, usas este push
```bash
git push -u origin nombre-de-tu-rama
```
El `u` hace que a partir de ahora cuando hagas algun push, pushee directamente en la rama.  \ 

Entonces, cada vez que arrancas:
```bash
git checkout nombre-de-tu-rama
git pull origin nombre-de-tu-rama
```
# Espero que les haya gustado mi acople con el Lol
