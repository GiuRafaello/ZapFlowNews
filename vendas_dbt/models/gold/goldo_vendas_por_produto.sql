WITH vendas_por_produto AS (
    SELECT
        produto,
        SUM(valor) AS total_valor,
        SUM(quantidade) AS total_quantidade,
        COUNT(*) AS total_vendas
    FROM {{ ref('silver_vendas') }}
    GROUP BY produto
)

SELECT
    produto,
    total_valor,
    total_quantidade,
    total_vendas
FROM
    vendas_por_produto
ORDER BY
    total_valor DESC
