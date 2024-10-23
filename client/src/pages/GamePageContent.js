import React,{ useState, useEffect }  from "react";
import axios from 'axios';
import { useRouter } from 'next/router';
import styles from '../styles/gamePageContent.module.css';
import { GameSection } from '../components/GameSection';
import NRL from '../assets/L.png';
import NR12 from '../assets/NR12.png';
import NR16 from '../assets/NR16.png';
import NR18 from '../assets/NR18.png';
import NR14 from '../assets/NR14.png';
import NR10 from '../assets/NR10.png';
import Image from "next/image";
import { Icon } from '@iconify/react';


export default function gamePage() {

    const [gameWiew, setGameWiew] = useState([]);

    const router = useRouter()
    
    const { gameId } = router.query

    
    useEffect(() => {

        CheckGames()

      }, []);

      const CheckGames = async () => {
        await axios.get(`http://127.0.0.1:5123/games/filter?game_id=${gameId}`)
        .then(response => {
            
            setGameWiew(response.data.game)

         })
      .catch(error => {

        

      });

    }

    const AddCart = () => {
        let currentGames = JSON.parse(localStorage.getItem('gameCartList')) || [];
        currentGames.push(gameWiew);
        localStorage.setItem('gameCartList', JSON.stringify(currentGames));
    }

  return (
    <div>
      <main className={styles.main}>
        <div className={styles.gameContainer}>
          <div className={styles.containerInfo}>
            <div className={styles.gameHeader}>
                <h1>{gameWiew.gameName} {gameWiew.secondGameName && gameWiew.secondGameName }</h1>
            </div>
            <div className={styles.gameMedia}>
            <iframe className={styles.gameVideo} width="960" height="380" src={gameWiew.videoPromotional} title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

            </div>
            <div className={styles.gameInfo}>
                <h2 className={styles.gameInfoTitle}>
                    Sobre esse game
                </h2>
                <p className={styles.gameInfoText}>
                    {gameWiew.description}
                </p>
            </div>
          </div>
            <div className={styles.gameDetails}>
                <div className={styles.priceSection}>
                <p className={styles.price}>R$ {gameWiew.price}</p>
                <p className={styles.detailsSectionTitle}><span className={styles.detailsSectionSpam}>Ativação: </span> { gameWiew.platform }</p>
                <p className={styles.detailsSectionTitleSpam}>
                    Produto ativado através de <a className={styles.textLink} href='https://google.com'>chave de ativação</a>
                </p>
                <p className={styles.titleGameBox}>
                    Ativações/ Sistemas
                </p>
                <div className={styles.gameBox}>
                    <p className={styles.nameGameBox}>
                    {gameWiew.gameName} {gameWiew.secondGameName && gameWiew.secondGameName }
                    </p>
                    {gameWiew.platform == "Steam" ? (
                        <div className={styles.iconsection}>
                            <Icon icon="mdi:steam"  style={{color: '#fff', fontSize: '1.2rem', marginRight: '0.2rem'}} />
                            <Icon icon="bi:windows"  style={{color: '#fff', fontSize: '1rem'}} />
                        </div>)
                    : (
                        <div className={styles.iconsection}>
                            <Icon icon="bi:windows"  style={{color: '#fff', fontSize: '1rem'}} />
                        </div>
                    )}

                </div>
                <p className={styles.nameGameBox} >Categoria/Gênero:</p>
                <p>{gameWiew.gender}</p>
                <div className={styles.sectionButton}>
                    <button className={styles.cartButton} onClick={AddCart}><Icon icon="mdi:cart-outline"  style={{color: '#100f0f', fontSize: '2rem'}} /> Adicionar ao Carrinho</button>
                    <button className={styles.favoriteButton}>
                        <Icon icon="ph:heart"  style={{color: '#607A8C', fontSize: '2rem'}} />
                    </button>
                </div>
                </div>
                <div className={styles.detailsSection}>
                <p className={styles.detailsSectionTitle}><span className={styles.detailsSectionTitleSpam}>Lançamento: </span> {gameWiew.year}</p>
                <p className={styles.detailsSectionTitle}><span className={styles.detailsSectionTitleSpam}>Desenvolvedor: </span> {gameWiew.creator}</p>
                <p className={styles.detailsSectionTitle}><span className={styles.detailsSectionTitleSpam}>Distribuidor: </span> {gameWiew.publisher}</p>
                <div>
                    <h2 className={styles.classifiedsSection}>
                        CLASSIFICAÇÃO INDICATIVA
                    </h2>

        <div className={styles.classifiedsSectionIcon}>
            <Image src= {NR16} width={50} height={50}/>
            <p className={styles.classifiedsSectionText}>
            NÃO RECOMENDADO PARA MENORES DE {gameWiew.ageGroup} ANOS
            </p>
        </div>

                </div>
                </div>
            </div>
        </div>

      <GameSection titleSection="Recomendados"/>
   
      </main>
    </div>
  );
}
