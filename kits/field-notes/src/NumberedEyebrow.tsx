import type { ReactNode } from 'react';

export interface NumberedEyebrowProps {
  /** The label itself — `HOW IT WORKS`. Uppercased by the stylesheet. */
  children: ReactNode;
  /** This section's position in the document. */
  index: number;
  /** How many sections the document has. A position needs a total to be one. */
  total: number;
  /** The wider 0.18em tracking the pack keeps for the roomier variant. */
  wide?: boolean;
  className?: string;
}

/** `03` from `3`, `09` from `9` — and `012` from `12` if the document is long. */
function pad(value: number, width: number): string {
  return String(value).padStart(width, '0');
}

/**
 * `〉 HOW IT WORKS [03/09]` — the pack's most transferable device, and the first
 * thing to keep when porting this look. The chevron and the position are drawn
 * by `::before` / `::after` off the `data-n` attribute, both at 55% opacity, so
 * the DOM carries only the label and the page numbers its own sections. A
 * marketing page with numbered sections stops being a brochure and becomes a
 * document with a table of contents.
 */
export function NumberedEyebrow({
  children,
  index,
  total,
  wide = false,
  className,
}: NumberedEyebrowProps) {
  const width = Math.max(2, String(total).length);
  return (
    <p
      className={['fn-eyebrow', wide ? 'fn-eyebrow--wide' : undefined, className]
        .filter(Boolean)
        .join(' ')}
      data-n={`[${pad(index, width)}/${pad(total, width)}]`}
    >
      {children}
    </p>
  );
}
