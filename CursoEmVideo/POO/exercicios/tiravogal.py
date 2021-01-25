def sem_vogal(txt):
        vogal = 'AEIOUaeiou'
        nova = ''
        for letra in txt:
            if letra not in vogal:
                nova = nova + letra
        return nova
    


palavra = 'Aredondado'
print(sem_vogal(palavra))
