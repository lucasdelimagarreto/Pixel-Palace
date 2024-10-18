import { Html, Head, Main, NextScript } from "next/document";

export default function Document() {
  return (
    <Html lang="pt-BR">
      <Head>
        <met charset="utf-8"/>
        <meta name="viewport" content="width=divice-width, initial-scale=1.0"/>
        <title>Pixel Palace</title>
      </Head>
      <body>
        <Main />
        <NextScript />
      </body>
    </Html>
  );
}