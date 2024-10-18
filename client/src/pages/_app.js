import '../styles/global.css'
import Header from '@/components/Header';
import Footer from '@/components/Footer';
import QualityTag from '@/components/QualityTag/QualityTag';

export default function App({ Component, pageProps }) {
  return <>
    <Header />
    <QualityTag />
    <Component {...pageProps} />
    <Footer />
  </>
}