coletados1, coletados2, coletados3 = map(int, input().split())
envenenados1, envenenados2, envenenados3 = map(int, input().split())

coletados = coletados1 + coletados2 + coletados3
envenenados = envenenados1 + envenenados2 + envenenados3

ovostotais = coletados - (envenenados * 2) - envenenados

print(ovostotais)