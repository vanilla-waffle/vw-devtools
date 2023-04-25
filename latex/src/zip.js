import dotenv from 'dotenv'
import { execSync } from 'child_process'

dotenv.config()

const path = process.env.REPOSITORY

execSync(`7z a -tzip output/vw-latex.zip ${path}/*`)