import { useId } from 'react';

export interface DuotoneProps {
  src: string;
  alt: string;
  size?: number;
  /** `round` for a chat avatar, `tile` for a large portrait. */
  shape?: 'round' | 'tile';
  className?: string;
}

/**
 * A photograph pushed through the pack's green duotone: desaturated, then mapped
 * through three stops (the field, the phosphor, the pale ink). The table values are
 * those stops written as fractions; an SVG filter cannot read a custom property, so
 * they move with the tokens by hand (see the pack's Gotchas).
 */
export function Duotone({ src, alt, size = 112, shape = 'tile', className }: DuotoneProps) {
  const id = `ph-duo-${useId().replace(/:/g, '')}`;
  return (
    <span
      className={['ph-duotone', `ph-duotone--${shape}`, className].filter(Boolean).join(' ')}
      style={{ width: size, height: size }}
    >
      <svg width="0" height="0" aria-hidden="true" focusable="false" style={{ position: 'absolute' }}>
        <filter id={id} colorInterpolationFilters="sRGB">
          <feColorMatrix type="saturate" values="0" />
          <feComponentTransfer>
            <feFuncR type="table" tableValues="0.01 0 0.84" />
            <feFuncG type="table" tableValues="0.02 1 1" />
            <feFuncB type="table" tableValues="0.02 0.4 0.89" />
          </feComponentTransfer>
        </filter>
      </svg>
      <img src={src} alt={alt} style={{ filter: `url(#${id}) contrast(1.15)` }} />
    </span>
  );
}
