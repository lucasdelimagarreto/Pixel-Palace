import React,{ useState, useEffect}  from "react";
import { Icon } from '@iconify/react';
import style from "./purchasedGamesCard.module.css"
import Image from 'next/image';



export default function PurchasedGamesCard () {

        const [visibleTokenId, setVisibleTokenId] = useState(null);
        
        const tokens = [
          { id: 1, token: Math.random().toString(36).substr(2) },
          { id: 2, token: Math.random().toString(36).substr(2) },
          { id: 3, token: Math.random().toString(36).substr(2) },
          { id: 4, token: Math.random().toString(36).substr(2) },
        ];

    const handleVisibility = (id) => {
        setVisibleTokenId(id);
          
    };    

    return (
        <section className={style.sectionConfig}>
            <div id={style.divInfos}>
                <h1>Minha conta</h1>
                <p>Jogos Adquiridos</p>
            </div>

            <div className={style.cardsSection}>
            <div className={style.cardSection}>
            <Image className={style.gameimg} src='https://assets.nuuvem.com/image/upload/t_banner_big/v1/products/557dbbf769702d0a9cc6c600/banners/qujvddkinximwmrl0apn.jpg' width={210} height={100} alt="Imagem gamecard" />
            <div>
                <div>
                    <p className={style.titlegamecard}>
                    Batman Arkham Knight
                    </p>
                        <div className={style.iconsection}>
                            <Icon icon="mdi:steam"  style={{color: '#27565e', fontSize: '1.2rem', marginRight: '0.2rem'}} />
                            <Icon icon="bi:windows"  style={{color: '#27565e', fontSize: '1rem'}} />
                        </div>
                </div>

                <div className={style.keyGameCard}>
                <button className={visibleTokenId === 1 ? style.keyButtonClic : style.keyButton}>
                {visibleTokenId === 1 ? Math.random().toString(36).substr(2) :  '------------------------'}
                {visibleTokenId !== 1 && (
                    <Icon onClick={() => handleVisibility(1)} icon="mdi:eye-off" width="2em" height="2em"  style={{color: '#96A6B7', marginLeft: '2rem'}} />
                )}
                {visibleTokenId == 1 && (
                    <Icon icon="ic:baseline-key" width="2em" height="2em"  style={{color: '#fff'}} />
                )}
                </button>
                    
                </div>
            </div>
        </div>

        <div className={style.cardSection}>
            <Image className={style.gameimg} src='https://assets.nuuvem.com/image/upload/t_banner_big/v1/products/557dbbf769702d0a9cc6c600/banners/qujvddkinximwmrl0apn.jpg' width={210} height={100} alt="Imagem gamecard" />
            <div>
                <div>
                    <p className={style.titlegamecard}>
                    Batman Arkham Knight
                    </p>
                        <div className={style.iconsection}>
                            <Icon icon="mdi:steam"  style={{color: '#27565e', fontSize: '1.2rem', marginRight: '0.2rem'}} />
                            <Icon icon="bi:windows"  style={{color: '#27565e', fontSize: '1rem'}} />
                        </div>
                </div>

                <div className={style.keyGameCard}>

                <button className={visibleTokenId === 2 ? style.keyButtonClic : style.keyButton}>
                {visibleTokenId === 2 ? Math.random().toString(36).substr(2) :  '------------------------'}
                {visibleTokenId !== 2 && (
                    <Icon onClick={() => handleVisibility(2)} icon="mdi:eye-off" width="2em" height="2em"  style={{color: '#96A6B7', marginLeft: '2rem'}} />
                )}
                {visibleTokenId == 2 && (
                    <Icon icon="ic:baseline-key" width="2em" height="2em"  style={{color: '#fff'}} />
                )}
                </button>
                    
                </div>
            </div>
        </div>

        <div className={style.cardSection}>
            <Image className={style.gameimg} src='https://assets.nuuvem.com/image/upload/t_banner_big/v1/products/557dbbf769702d0a9cc6c600/banners/qujvddkinximwmrl0apn.jpg' width={210} height={100} alt="Imagem gamecard" />
            <div>
                <div>
                    <p className={style.titlegamecard}>
                    Batman Arkham Knight
                    </p>
                        <div className={style.iconsection}>
                            <Icon icon="mdi:steam"  style={{color: '#27565e', fontSize: '1.2rem', marginRight: '0.2rem'}} />
                            <Icon icon="bi:windows"  style={{color: '#27565e', fontSize: '1rem'}} />
                        </div>
                </div>

                <div className={style.keyGameCard}>

                <button className={visibleTokenId === 3 ? style.keyButtonClic : style.keyButton}>
                {visibleTokenId === 3 ? Math.random().toString(36).substr(2) :  '------------------------'}
                {visibleTokenId !== 3 && (
                    <Icon onClick={() => handleVisibility(3)} icon="mdi:eye-off" width="2em" height="2em"  style={{color: '#96A6B7', marginLeft: '2rem'}} />
                )}
                {visibleTokenId == 3 && (
                    <Icon icon="ic:baseline-key" width="2em" height="2em"  style={{color: '#fff'}} />
                )}
                </button>
                    
                </div>
            </div>
        </div>

        <div className={style.cardSection}>
            <Image className={style.gameimg} src='https://assets.nuuvem.com/image/upload/t_banner_big/v1/products/557dbbf769702d0a9cc6c600/banners/qujvddkinximwmrl0apn.jpg' width={210} height={100} alt="Imagem gamecard" />
            <div>
                <div>
                    <p className={style.titlegamecard}>
                    Batman Arkham Knight
                    </p>
                        <div className={style.iconsection}>
                            <Icon icon="mdi:steam"  style={{color: '#27565e', fontSize: '1.2rem', marginRight: '0.2rem'}} />
                            <Icon icon="bi:windows"  style={{color: '#27565e', fontSize: '1rem'}} />
                        </div>
                </div>

                <div className={style.keyGameCard}>

                <button className={visibleTokenId === 4 ? style.keyButtonClic : style.keyButton}>
                {visibleTokenId === 4 ? Math.random().toString(36).substr(2) :  '------------------------'}
                {visibleTokenId !== 4 && (
                    <Icon onClick={() => handleVisibility(4)} icon="mdi:eye-off" width="2em" height="2em"  style={{color: '#96A6B7', marginLeft: '2rem'}} />
                )}
                {visibleTokenId == 4 && (
                    <Icon icon="ic:baseline-key" width="2em" height="2em"  style={{color: '#fff'}} />
                )}
                </button>
                    
                </div>
            </div>
            </div>
        </div>
        </section>
    )
}