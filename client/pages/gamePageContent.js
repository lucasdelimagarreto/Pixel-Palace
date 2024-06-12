import Head from 'next/head';
import React,{ useState, useEffect }  from "react";
import axios from 'axios';
import { useRouter } from 'next/router';
import Header from '../components/Header';
import QualityTag from '../components/QualityTag';
import Footer from '../components/Footer';
import styles from '../styles/gamePageContent.module.css';
import { GameSection } from '../components/GameSection';
import NR16 from '../assets/NR16.png';
import Image from "next/image";
import { Icon } from '@iconify/react';


export default function gamePage() {

    const router = useRouter()
    
    const { gameId } = router.query

    const [listGames, setListGames] = useState([]);
    
    useEffect(() => {

        CheckGames()

      }, []);

      const CheckGames = () => {
        axios.get(`http://192.168.0.7:5123/games/filter?game_id=${gameId}`)
        .then(response => {
            
            setListGames(response.data.game)
            

         })
      .catch(error => {

        

      });

    }
    
  return (
    <div>
            <Head>
                <met charset="utf-8"/>
                <meta name="viewport" content="width=divice-width, initial-scale=1.0"/>
                <title>Pixel Palace</title>
            </Head>
            <Header/>

      <main className={styles.main}>
        <QualityTag/>
        {listGames && listGames.map(game => (
        <div className={styles.gameContainer}>
          <div className={styles.containerInfo}>
            <div className={styles.gameHeader}>
                <h1>{game.gameName} {game.secondGameName && game.secondGameName }</h1>
            </div>
            <div className={styles.gameMedia}>
            <iframe className={styles.gameVideo} width="960" height="380" src="https://www.youtube.com/embed/W2Yjqfkzc_w?si=v1Cx10WdgtLxQSUE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

            </div>
            <div className={styles.gameInfo}>
                <h2 className={styles.gameInfoTitle}>
                    Sobre esse game
                </h2>
                <p className={styles.gameInfoText}>
                Batman: Arkham Origins™ é o novo capítulo da franquia de grande sucesso Batman: Arkham.
                O jogo apresenta uma cidade de Gotham ainda maior e introduz um prólogo original que é 
                situado vários anos antes dos eventos de Batman: Arkham Asylum e Batman: Arkham City, 
                os dois primeiros sucessos desta franquia. Surgindo antes da ascensão dos criminosos 
                mais perigosos de Gotham City, o jogo apresenta um Batman novo e refinado enquanto ele 
                segue um momento decisivo de sua carreira como um combatente do crime em seu caminho 
                para se tornar definitivamente o Cavaleiro das Trevas. No desenrolar da história, 
                jogadores encontrarão vários personagens importantes pela primeira vez e vão forjar 
                parcerias chaves.
                </p>
            </div>
          </div>
            <div className={styles.gameDetails}>
                <div className={styles.priceSection}>
                <p className={styles.price}>R$ {game.price}</p>
                <p className={styles.detailsSectionTitle}><span className={styles.detailsSectionSpam}>Ativação: </span> Steam</p>
                <p className={styles.detailsSectionTitleSpam}>
                    Produto ativado através de <a className={styles.textLink} href='google.com'>chave de ativação</a>
                </p>
                <p className={styles.titleGameBox}>
                    Ativações/ Sistemas
                </p>
                <div className={styles.gameBox}>
                    <p className={styles.nameGameBox}>
                    {game.gameName} {game.secondGameName && game.secondGameName }
                    </p>
                    {game.plataform === "Steam" ? (
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
                <p>Ação, Aventura, Furto, Luta</p>
                <div className={styles.sectionButton}>
                    <button className={styles.cartButton}><Icon icon="mdi:cart-outline"  style={{color: '#100f0f', fontSize: '2rem'}} /> Adicionar ao Carrinho</button>
                    <button className={styles.favoriteButton}>
                        <Icon icon="ph:heart"  style={{color: '#607A8C', fontSize: '2rem'}} />
                    </button>
                </div>
                </div>
                <div className={styles.detailsSection}>
                <p className={styles.detailsSectionTitle}><span className={styles.detailsSectionTitleSpam}>Lançamento: </span> 25/10/2013</p>
                <p className={styles.detailsSectionTitle}><span className={styles.detailsSectionTitleSpam}>Desenvolvedor: </span> WB Games Montreal</p>
                <p className={styles.detailsSectionTitle}><span className={styles.detailsSectionTitleSpam}>Distribuidor: </span> Warner Bros. Games</p>
                <div>
                    <h2 className={styles.classifiedsSection}>
                        CLASSIFICAÇÃO INDICATIVA
                    </h2>
                    <div className={styles.classifiedsSectionIcon}>
                        <Image src= {NR16} width={50} height={50}/>
                        <p className={styles.classifiedsSectionText}>
                            NÃO RECOMENDADO PARA MENORES DE 16 ANOS
                        </p>
                    </div>
                </div>
                </div>
            </div>
        </div>))}

      <GameSection titleSection="Recomendados"/>
   
      </main>
      <Footer/>
    </div>
  );
}
