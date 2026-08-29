export interface PortraitProps {
  /** The product screenshot — a flat still, never in browser chrome. */
  src: string;
  alt: string;
  className?: string;
}

export function Portrait({ src, alt, className }: PortraitProps) {
  return (
    <img className={['sv-portrait', className].filter(Boolean).join(' ')} src={src} alt={alt} />
  );
}
