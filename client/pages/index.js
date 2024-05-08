import Head from 'next/head';
import QualityTag from '../components/QualityTag';
import Header from '../components/Header';
import Footer from '../components/Footer';
import GameSection from '../components/GameSection';
import { useRouter } from 'next/router';

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
                <GameSection/>
                <GameSection/>
                <GameSection/>
                <GameSection/>
                <GameSection/>
            </main>

            <Footer/>
        </div>
    )
}