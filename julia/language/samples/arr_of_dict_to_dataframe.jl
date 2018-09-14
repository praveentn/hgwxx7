using HTTP, JSON

function getBody(resp)
    jsonb=String(resp.body)
    bodyData = JSON.parse(jsonb)
end

function histoday()
    base_url="https://min-api.cryptocompare.com"
    path= "data/histoday?fsym=BTC&tsym=USD&limit=100"
    url="$base_url/$path"
    bd = getBody(HTTP.get(url))["Data"]
end

x = histoday()
# vcat(DataFrame.(x)...)
