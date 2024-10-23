import React,{ useState, useEffect}  from "react";
import style from "../styles/cart.module.css"
import { Icon } from "@iconify/react";
import bntStyle from "../styles/buttons.module.css"
import { GameCardBuy } from '@/components/GameCardBuy';



export default function Cart () {
    return (
        <main className={style.mainCart}>
            <h1>Meu Carrinho</h1>

            <section className={style.sectionCart}>
                <div className={style.productsSection}>

                    <h2>Produtos</h2>
                    
                    <GameCardBuy />

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
                            <p>R$ 00</p>
                        </div>

                        <button className={bntStyle.bntGreenNoBorder}>Continuar</button>

                    </div>

                </div>
            </section>
        </main>
    )
}