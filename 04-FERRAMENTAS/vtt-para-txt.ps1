# Converte todos os .vtt de uma pasta em .txt limpo (sem tempos, sem linhas repetidas).
# Uso: .\vtt-para-txt.ps1 -Pasta "D:\ESCOLA DE SEO - Conhecimento extraido\05-LEGENDAS-BRUTAS"
param([Parameter(Mandatory)][string]$Pasta)

Get-ChildItem $Pasta -Filter *.vtt | ForEach-Object {
    $linhas = Get-Content $_.FullName -Encoding UTF8 |
        Where-Object { $_ -and $_ -notmatch '^(WEBVTT|NOTE|X-TIMESTAMP|\d+$)' -and $_ -notmatch '-->' } |
        ForEach-Object { ($_ -replace '<[^>]+>', '').Trim() } |
        Where-Object { $_ }

    $saida = New-Object System.Collections.Generic.List[string]
    foreach ($l in $linhas) { if ($saida.Count -eq 0 -or $saida[$saida.Count - 1] -ne $l) { $saida.Add($l) } }

    $destino = [IO.Path]::ChangeExtension($_.FullName, '.txt')
    ($saida -join ' ') | Set-Content -Path $destino -Encoding UTF8
    Write-Host "OK: $destino ($($saida.Count) linhas)"
}
