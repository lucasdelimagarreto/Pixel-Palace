import { useRouter } from 'next/router';
import Head from 'next/head';
import QualityTag from '../components/QualityTag';
import Header from '../components/Header';
import Footer from '../components/Footer';
import {GameSection} from '../components/GameSection';

export default function HomePage() {
    return(
        <div>
            <Head>
                <met charset="utf-8"/>
                <meta name="viewport" content="width=divice-width, initial-scale=1.0"/>
                <title>Pixel Palace</title>
            </Head>

            <Header/>

            <main>
                <QualityTag/>
                <GameSection titleSection={"Jogos novos"} subTitleSection={"Jogos recém adicionados!"}/>
                <GameSection titleSection={"Ofertas"} subTitleSection={"Jogos com até 95% de desconto!"}/>
                <GameSection titleSection={"Ofertas"} subTitleSection={"Jogos com até 95% de desconto!"}/>
                <GameSection titleSection={"Ofertas"} subTitleSection={"Jogos com até 95% de desconto!"}/>
                <GameSection titleSection={"Ofertas"} subTitleSection={"Jogos com até 95% de desconto!"}/>
            </main>

            <Footer/>
        </div>
    )
}