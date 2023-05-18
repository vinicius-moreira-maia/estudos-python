'''
posso ter varios tipos de exceções em um só except:
    except(ValueError, IndexError):
        ...
vários excepts:
    except ValueError:
        ...
    except IndexError:
        ...
ou somente except para qualquer exceção:
    except:
        ... 

'''

# função polimórfica
def readVal(valType, requestMsg, errorMsg):
    while True:
        val = input(requestMsg + ' ')
        try:
            # converte str para valType antes de retornar
            return valType(val)
        except ValueError:
            print(val, errorMsg)

readVal(int, 'Enter an integer:', 'is not an integer')