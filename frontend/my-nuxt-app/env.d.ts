/// <reference types="nuxt3" />

interface ImportMetaEnv {
  readonly NUXT_PUBLIC_MAIN_URL: string
}

interface ImportMeta {
  readonly env: ImportMetaEnv
}
