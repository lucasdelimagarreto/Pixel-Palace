import React,{ useState, useEffect}  from "react";
import style from "../styles/cart.module.css"
import { Icon } from "@iconify/react";
import Image from 'next/image';
import bntStyle from "../styles/buttons.module.css"
import { useRouter } from 'next/router';


export default function Cart () {

    const router = useRouter()
    const [cartList, setCartList] = useState();
    const [cartPrice, setCartPrice] = useState(0);

    useEffect(() => {

        const storedGameCartList = localStorage.getItem('gameCartList');

        if (storedGameCartList) {

          const foundStoredGameCartList = JSON.parse(storedGameCartList);

          setCartList(foundStoredGameCartList);


        }
      }, []);

      const deleteGameFromLocalStorage = (gameId) => {
        const storedGames = JSON.parse(localStorage.getItem('gameCartList')) || [];
        
        const updatedGames = storedGames.filter(game => game.id !== gameId);
    
        localStorage.setItem('gameCartList', JSON.stringify(updatedGames));

        setCartList(updatedGames)
      };
      
      
      useEffect(() => {
        const storedGames = JSON.parse(localStorage.getItem('gameCartList')) || [];

        const totalPrice = storedGames.reduce((acc, game) => acc + game.price, 0);
        setCartPrice(totalPrice);
      }, [cartList]);


      console.log(cartPrice)

    return (
        <main className={style.mainCart}>
            <h1>Meu Carrinho</h1>

            <section className={style.sectionCart}>
                <div className={style.productsSection}>

                    <h2>Produtos</h2>
                    
                    {cartList && cartList.map(game => (
        <div className={style.cardSection}>
            <Image className={style.gameimg} src={game.imageBanner} width={210} height={100} alt="Imagem gamecard" />
            <div>
                <div>
                    <p className={style.titlegamecard}>
                        {game.gameName} {game.secondGameName && game.secondGameName }
                    </p>
                    
                        {game.platform == "Steam"? (
                        <div className={style.iconsection}>
                            <Icon icon="mdi:steam"  style={{color: '#27565e', fontSize: '1.2rem', marginRight: '0.2rem'}} />
                            <Icon icon="bi:windows"  style={{color: '#27565e', fontSize: '1rem'}} />
                        </div>)
                    : (
                        <div className={style.iconsection}>
                            <Icon icon="bi:windows"  style={{color: '#27565e', fontSize: '1rem'}} />
                        </div>
                    )}
                </div>

                <div className={style.buyGameCard}>
                    <a>
                        <button className={style.buttongamecard} onClick={() => {router.push(`../../GamePageContent?gameId=${game.id}`)}}>
                        R$ {game.price.toFixed(2)}
                        </button>
                    </a>

                    <button className={style.trashButton} onClick={() => deleteGameFromLocalStorage(game.id)}>
                        <Icon icon="jam:trash-f" width="2rem" height="2rem"  style={{color: '#96A6B7'}} />
                    </button>

                </div>
            </div>
        </div>))}

                </div>

                <div className={style.paymentSection}>
                    <div className={style.paymentMethods}>
                        <h2>Forma de Pagamento</h2>
                        <ul className={style.paymentCards}>
                            <li>
                                <Icon icon="stash:pix" width="5rem" height="5rem"  style={{color: '#0F2124'}} />
                                <p>PIX</p>
                            </li>
                            <li>
                                <Icon icon="bi:credit-card-fill" width="5rem" height="5rem"  style={{color: '#0F2124'}} />
                                <p>Cartão</p>
                            </li>
                            <li>
                                <Icon icon="majesticons:paper-fold-text" width="5rem" height="5rem"  style={{color: '#0F2124'}} />
                                <p>Boleto</p>
                            </li>
                        </ul>

                    </div>
                    <div className={style.buySection}>
                        <div>
                            <h2>Valor total</h2>
                            <p>R$ {cartPrice.toFixed(2)}</p>
                        </div>

                        <button className={bntStyle.bntGreenNoBorder}>Continuar</button>

                    </div>

                </div>
            </section>
        </main>
    )
}