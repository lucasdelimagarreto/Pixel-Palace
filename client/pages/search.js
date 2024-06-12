import { useRouter } from 'next/router';
import Head from 'next/head';
import Header from '../components/Header';
import QualityTag from '../components/QualityTag';
import Footer from '../components/Footer';
import { GameSectionSearch} from '../components/GameSection';


export default function Search (){
    const router = useRouter();
    const { searchImput } = router.query
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
               <GameSectionSearch searchImput={searchImput}/>

            </main>
            <Footer/>
        </div>
    )
}