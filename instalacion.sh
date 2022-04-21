echo "Bienvenido al asistente de instalacion de ScanLite, vamos a empezar por instalar las librerias de python."
pip install socket
pip install sys
echo "Si te da error significa que ya las tienes instaladas o que tu version de python no es la adecuada, recuerda, Python3"
echo "ahora vamos a darle permisos de ejecucion al script, esto SOLO FUNCIONA EN SISTEMAS UNIX-LIKE"
chmod +x scanlite.py
echo "Ahora solo pon en tu consola "./scanlite.py" ya tienes el script listo"
echo "Gracias por instalar ScanLite, ahora vamos a borrar este instalador"
rm instalacion.sh
