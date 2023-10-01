echo "--------------------------"
echo "Deteniendo contenedores"
echo "--------------------------"

docker compose down

echo "--------------------------"
echo "Iniciando contenedores"
echo "--------------------------"

docker compose up -d
