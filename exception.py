def main():
    try:
        no1=int(input("enter first number"))
        no2=int(input("enter second number"))
    
        ans=no1/no2
        print("division is",ans)
    except ZeroDivisionError:
        print("----------------exception occured-------------")
    except ValueError:
        print("---------------- value error!---------------------")
    except Exception:
        print("inside last except block")
    finally:
        print("inside FINALLY block")
if __name__=="__main__":
    main()